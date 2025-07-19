# Week 5
# Bitly

## 1. 시스템 설계 프레임워크
1. 요구사항 정의
    - 기능적 요구사항 (Functional Requirements)
    - 비기능적 요구사항 (Non-functional Requirements)

2. 핵심 엔티티 정의
    - 저장되거나 교환되는 주요 데이터 구조

3. API 정의
    - 사용자와 백엔드 간의 인터페이스

4. High-Level Design
    - 기능 요구사항을 만족하는 기본 아키텍처 구성

5. Deep Dive
    - 비기능 요구사항을 만족시키기 위한 구조 고도화

---

## 2. 기능 요구사항

- 사용자는 긴 URL을 단축된 short URL로 변환할 수 있어야 한다.
- short URL 요청 시 원래의 long URL로 리디렉션되어야 한다.
- 사용자는 커스텀 alias를 지정할 수 있어야 한다. (선택 사항)
- 단축 URL에 만료 시간을 설정할 수 있어야 한다. (선택 사항)

---

## 3. 비기능 요구사항

- 리디렉션은 200ms 이하의 낮은 지연 시간으로 응답해야 한다.
- 시스템은 1억 일일 사용자와 10억 개 이상의 URL을 처리할 수 있어야 한다.
- shortCode는 충돌 없이 고유해야 한다.
- 일부 서버 장애 상황에서도 서비스는 고가용성을 유지해야 한다.
- consistency보다는 availability를 우선하며 eventual consistency를 허용할 수 있다.

---

## 4. 핵심 엔티티

- URL
    - shortCode
    - originalUrl
    - expirationTime
    - creationTime
    - userId

- User
    - userId
    - email, password 등의 기타 필드

---

## 5. API 정의

### POST /urls
- 긴 URL을 단축 URL로 변환
- 요청 본문:
    - originalUrl (필수)
    - customAlias (선택)
    - expirationTime (선택)
- 응답: short URL

### GET /:shortCode
- shortCode를 통해 원래 URL로 리디렉션
- 유효하지 않거나 만료된 경우 에러 응답

---

## 6. 초기 아키텍처 (High-Level Design)

기본 구성: 클라이언트 → 서버 → 데이터베이스

- POST 요청:
    - shortCode 생성 → DB에 저장
- GET 요청:
    - shortCode 조회 → longUrl 반환 → 302 Redirect

---

## 7. Deep Dive

### 7-1. shortCode 생성 전략

1. 랜덤 숫자 + Base62 인코딩
    - 충돌 가능 → DB 중복 확인 필요
2. Hash(longUrl) + Base62
    - 충돌 가능 → DB 확인 필요
3. **카운터 + Base62 인코딩**
    - 충돌 없음, 단 예측 가능성 존재
4. **카운터 + 양방향 함수(Bijective Function)**
    - Squids.io 등 활용하여 난독화 및 보안 향상

### 7-2. 리디렉션 성능 최적화

- shortCode 필드에 인덱스 적용 (Primary Key)
- Redis를 활용한 Read-through LRU 캐시 도입
- CDN은 분석 불가 단점으로 인해 일반적으로 사용하지 않음 (302 Redirect 선호)

### 7-3. 확장성 대응

- 읽기와 쓰기 서버 분리 (ReadService / WriteService)
- API Gateway를 통해 요청 라우팅
- 서버는 수평 확장 (Auto Scaling)
- 글로벌 카운터는 Redis INCR 사용
- 사전 할당 방식으로 성능 최적화 가능

### 7-4. 데이터베이스 처리

- 평균 URL 레코드 크기: 약 500바이트
- 10억 개 URL = 500GB → 단일 인스턴스로 수용 가능
- 필요시 shortCode 기준 샤딩 고려 가능

### 7-5. 고가용성 설계

- Redis는 장애 발생 시 DB로 fallback
- Redis Global Counter는 단일 장애점 → 고가용성 모드 설정 필요
- 데이터베이스는 Replication 구성 및 S3에 스냅샷 백업 수행

---

## 8. 설계 전략 요약

- 기능 → 구조 → 비기능 요구사항 순으로 설계
- 설계 선택의 근거(트레이드오프)를 명확히 설명할 수 있어야 함
- 무의미한 계산은 피하고, 설계 결정을 위한 계산만 수행
- 기술 자체보다 "왜 이 기술을 선택했는가"를 설명하는 것이 중요함
