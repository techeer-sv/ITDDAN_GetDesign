# Ad Click Aggregator

-   웹사이트에 광고가 표시될 때 사용자가 클릭하는 광고 클릭 데이터를 수집하고 집계하는 시스템
-   광고주에게 광고의 효율성(클릭 수, 기간별 클릭 수 등)에 대한 지표 제공

## 비기능적 요구사항

-   광고 수: 동시에 1천만 개의 광고 지원
-   초당 광고 클릭 수 (CPS): 피크 시 초당 10,000회 클릭 처리

-   확장성 (Scalability): 초당 10,000회 클릭의 피크를 지원할 수 있어야 함
-   낮은 지연 시간 (Low Latency): 분석 쿼리의 지연 시간은 1초 미만이어야 함
-   결함 허용 (Fault Tolerant) 및 높은 데이터 무결성 (High Data Integrity): 클릭 데이터를 손실하지 않아야 함 => 이 데이터는 광고주 지불금에 영향을 미치므로 정확해야 함!
-   실시간 처리 (Real-Time): 분석 쿼리 데이터는 최소 1분 단위로 최대한 최신 상태여야 함
-   광고 클릭의 항등성 (Idempotency of Ad Clicks): 사용자가 하나의 특정 광고를 여러 번 클릭하더라도 한 번만 카운트되어야 함 (스팸 방지)

---

## 흐름

1. 클릭 데이터가 시스템에 들어옴
2. 사용자가 리디렉션됨
3. 클릭 데이터를 검증하여 항등성 문제 처리
4. 클릭 데이터(원시 클릭 데이터) 로그
5. 클릭 데이터 집계
6. 집계된 데이터가 광고주에 의해 쿼리됨

## 설계 방식

1. 광고 배치 서비스가 브라우저에 redirect_URL을 직접 보내고, 브라우저가 클릭 후 바로 리디렉션하면서 클릭 이벤트를 병렬로 클릭 처리 서비스에 보냄

-   문제점: 악의적인 사용자나 광고 차단기는 redirect_URL을 DOM에서 직접 추출하여 클릭 처리 서비스에 클릭 이벤트를 보내지 않고도 리디렉션될 수 있음

2. 광고 배치 서비스는 ad_ID만 브라우저에 보냄 [나은 방식]

-   사용자가 광고를 클릭하면 브라우저는 ad_ID를 포함한 클릭 이벤트를 클릭 처리 서비스로 보냄
-   클릭 처리 서비스는 ad_ID를 사용하여 Ads DB에서 redirect_URL을 가져옴
-   클릭이 성공적으로 로그되면 클릭 처리 서비스는 redirect_URL과 함께 302 리디렉션 응답을 브라우저에 반환함

---

## 쿼리 성능 문제

1.  Spark (MapReduce 작업) 도입

-   클릭 DB에서 데이터를 주기적으로 (예: 5분마다) 읽어와 집계함
-   집계된 데이터를 읽기 최적화된 OLAP 데이터베이스에 저장하여 광고주 쿼리 속도를 높임
-   두 개의 DB 분리 이유: 읽기/쓰기 워크로드 간의 경쟁 감소 및 오류 격리
-   한계: 여전히 실시간성 부족

2. Spark 대신 스트림(Stream) (예: Kinesis 또는 Kafka) 도입

-   클릭 처리 서비스가 실시간으로 클릭 이벤트를 스트림에 발행함
-   스트림 애그리게이터(Stream Aggregator) (예: Flink)가 스트림에서 실시간으로 이벤트를 읽어 인메모리에서 집계함
-   애그리게이션 윈도우(Aggregation Window) (예: 1분)를 정의하여 1분마다 집계된 데이터를 읽기 최적화된 DB에 쓰기 작업
-   플러시 간격(Flush Interval) (예: 10초)을 설정하여 부분적인 집계 결과를 더 자주 DB에 기록함 (광고주가 거의 실시간으로 부분 데이터를 확인할 수 있도록)
