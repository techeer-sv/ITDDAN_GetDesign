# Week 4
Created on 2025-06-22

# Change Data Capture(CDC)란?
**CDC (Change Data Capture)** 는 데이터베이스에서 발생한 변경 사항을 실시간으로 감지하고, 이를 다른 시스템(예: Elasticsearch, Redis, 캐시, 데이터 웨어하우스 등)에 전달하는 기술

### 주요 사용 목적:
- 검색 인덱스 자동 동기화 (Elasticsearch)
- 데이터 분석 파이프라인 연동 (Spark, Hadoop 등)
- 다른 마이크로서비스/시스템과의 이벤트 전파
- 분산 캐시 자동 갱신 (Redis 등)

### MongoDB CDC 전파 방법
1. MongoDB Change Streams
2. Kafka
3. Redis Streams
4. 등등

### 전파시 고려사항
1. 멱등성 보장: 같은 이벤트가 중복 처리되더라도 결과는 동일해야 함
   - 이유:
     - 네트워크 장애, 재시도 로직, 컨슈머 장애 복구 등으로 인해 이벤트가 중복 전송되는 경우가 빈번함
     - 중복 이벤트로 인해 Elasticsearch 인덱스가 꼬이거나, Kafka에 쌓인 이벤트가 여러 번 소비되는 문제 방지
   - 구현 전략:
     - 외부 시스템에서 document_id를 기준으로 덮어쓰기(upsert) 처리 
     - 이벤트에 event_id 또는 version, timestamp를 포함해 이전에 처리된 이벤트인지 판단 
     - 업데이트가 아닌 patch/merge 형태로 적용할 경우, 이벤트 해시 비교를 통해 중복 여부 판단
2. 이벤트 순서 보장: 동일 문서에 대한 변경은 순서대로 처리해야 정합성 유지
   - 이유:
     - 병렬 처리 환경 (멀티 스레드, 멀티 인스턴스)에서 이벤트가 뒤바뀌어 도착할 수 있음 
     - 네트워크 지연이나 재처리 중 과거 이벤트가 나중에 수신될 수 있음
   - 구현 전략:
     - 이벤트에 타임스탬프 혹은 버전 정보(version) 포함 → 최신 이벤트만 처리 
     - Kafka 등 메시지 큐에서는 **파티션 키 설정(keyed partitioning)**으로 리소스 단위 순서 보장 
     - Consumer 측에서 리소스 단위 락 또는 단일 쓰레드 처리 큐 구성
3. 장애 복구: 실패 시 재시작 가능
    - 이유:
      - 실시간 CDC 처리는 장시간 실행되며, 프로세스 중단 시 전체를 다시 처리하는 것은 비효율적 
      - 데이터 유실 없이 "이어서" 처리하는 기능이 필수
    - MongoDB 예시:
      - MongoDB Change Stream은 resumeToken이라는 특수 토큰을 사용하여 중단 시점부터 재시작 가능 
      - 애플리케이션은 이 토큰을 안전하게 저장하고, 장애 발생 시 이를 이용해 다시 연결 가능 
    - Kafka 예시:
      - Kafka는 offset 기반 재시작을 지원 → Consumer는 마지막 커밋된 offset 이후부터 재시작 가능 
    - 구현 전략:
      - resumeToken, lastProcessedTimestamp, lastOffset 등의 메타데이터를 별도 저장소(DB, Redis 등)에 기록 
      - 처리 성공 이후에만 커밋(commit) or 토큰 저장 → at-least-once 처리를 보장
4. 백오프 전략: 과부하일 경우 일시 지연 처리 필요 
   - 이유:
     - 데이터베이스는 빠르게 변경되지만, 전파 대상 시스템의 처리 속도가 이를 따라가지 못할 수 있음 
     - 이때 전송을 강행하면 큐가 폭주하거나 외부 시스템 장애로 이어질 수 있음 
   - 구현 전략:
     - 지수적 백오프(Exponential Backoff): 실패 시 대기 시간을 점점 늘리며 재시도 
     - Circuit Breaker 패턴: 일정 오류율 이상이면 일시적으로 CDC 처리를 차단 
     - Rate Limiter (속도 제한기): 외부 시스템의 TPS 초과 방지 
     - Queue-based decoupling: 내부 큐(Redis, Kafka 등)에 임시 적재하여 속도 차를 흡수
