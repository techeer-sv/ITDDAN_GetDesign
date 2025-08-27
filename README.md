# ITDDAN_GetDesign

```bash
$ ITDDAN_GetDesign> ./study build system_architecture --mode=deep-dive --source=realworld
```

---

## 규칙

- **주 1회 진행**: 날짜 및 시간은 구성원 합의합니다.
- **입장권**: 코테 한 문제는 최소한의 마음가짐입니다.
- **질문은 자유**: 많이 질문 합시다.

---

## 방식

- 매 회차, 사례(인터뷰/문서/영상 등)를 선정해 함께 분석합니다.
- 사례 속 기술 키워드 중 각자 관심 있는 주제를 공부 및 정리해 와서 공유합니다.

---

## 입장권 안내

각자 코딩 테스트 **한 문제 이상을 풀어오며**, 그 결과를 자동화된 시스템을 통해 검증받습니다.

- **지원 언어**: Python, Java, JavaScript, Go
- **자동화 기능**: PR 생성 시 → 린트 검사 → 코드 실행 → 리뷰어 자동 지정

각 언어별 린트 및 실행 방식은 아래 가이드를 참고하세요:

- [Python 린팅 가이드](./docs/LINTING_PYTHON.md)
- [Java 린팅 가이드](./docs/LINTING_JAVA.md)
- [JavaScript 린팅 가이드](./docs/LINTING_JAVASCRIPT.md)
- [Go 린팅 가이드](./docs/LINTING_GO.md)

---

## 브랜치 & PR 규칙

### 브랜치 네이밍

- 스터디 주차 브랜치: `week{N}-{이름}` (예: week9-jungeun)
- 기타 브랜치: 목적에 맞는 이름 사용(이슈에서 생성되는 대로) (예: fix-python-lint, update-ci-config)

### Github actions 로컬 테스트 및 커밋 관리

- 다음 가이드를 따라 act 설치
- [Github actions 로컬 자동화 테스트 가이드](./bin/README.md)
- act 설치 후, git bash에서 자동화 테스트를 해볼 수 있습니다.

```bash
./bin/test_and_commit.sh
```

### 커밋 메시지

- 코딩테스트: **로컬 테스트 및 커밋 관리** 실행 후 자동 커밋됨 (예: `feat: 업데이트 Modified files: [파일목록]` )
- 아키텍처 분석: `Week{N} {영상/자료명} 제출` (예: Week9 Netflix System Design 제출)
  - 영상 하나당 하나의 커밋으로 작성

### PR(Pull Request)

- PR 제목: `Week{N} {이름}` (예: Week9 Jungeun)
- PR은 스터디 주차에 맞춰서 생성
- PR 설명에는 다음 내용을 반드시 포함:

  - 구현한 내용 요약
  - 리뷰어는 로컬에서 아래의 방법으로 테스트할 수 있습니다.

    ```bash
    # Python
    $ python3 파일명.py

    # Java
    $ javac -d target/classes 파일명.java
    $ cd target/classes
    $ java 패키지.클래스명

    # JavaScript
    $ node 파일명.js

    # Go
    $ go run 파일명.go
    ```

### 코드 리뷰 규칙

- PR 작성자

  - 리뷰 코멘트에 대한 응답은 모두 작성
  - 코드 수정 후에는 리뷰어에게 Re-review 요청 (소용돌이 버튼 클릭)
  - 피드백을 반영한 경우, 해당 커밋 링크를 코멘트로 남기기
  - 모든 리뷰어가 Approve 했다면 직접 Merge 진행

- 리뷰어
  - 할당된 PR은 책임감을 가지고 리뷰
  - 리뷰 완료 후 반드시 Approve 진행
  - 시스템 설계 및 구현에 대해서도 적극적인 리뷰 권장
