# ITDDAN_GetDesign
```bash
$ ITDDAN_GetDesign> ./study build system_architecture --mode=deep-dive --source=realworld
```
---
## 규칙
* **주 1회 진행**: 날짜 및 시간은 구성원 합의합니다.
* **입장권**: 코테 한 문제는 최소한의 마음가짐입니다.
* **질문은 자유**: 많이 질문 합시다.

---
## 방식
* 매 회차, 사례(인터뷰/문서/영상 등)를 선정해 함께 분석합니다.
* 사례 속 기술 키워드 중 각자 관심 있는 주제를 공부 및 정리해 와서 공유합니다.
----

## 입장권 안내
각 언어별로 자동화된 코드 품질 검사를 제공합니다.

### 지원 언어
이 프로젝트는 코딩 테스트 문제 해결을 위해 아래의 언어를 지원합니다.
- **Python** (.py)
- **Java** (.java)
- **JavaScript** (.js)
- **Go** (.go)

### 코드 품질 가이드
코드를 작성하고 Pull Request를 생성하기 전, 각 언어별 '린팅 가이드'에 따라 코드 품질을 점검해주세요.

| 언어             | 상세 린팅 가이드                                         |
|:---------------|:--------------------------------------------------|
| **Python**     | [Python 린팅 가이드](./docs/LINTING_PYTHON.md)         |
| **JavaScript** | [JavaScript 린팅 가이드](./docs/LINTING_JAVASCRIPT.md) |
| **Java**       | [Java 린팅 가이드](./docs/LINTING_JAVA.md)             |
| **Go**         | [Go 린팅 가이드](./docs/LINTING_GO.md)                 |

-----

## CI/CD 워크플로우

GitHub Actions를 통해 자동으로 다음 작업들이 수행됩니다:

1.  **파일 변경 감지** - 수정된 코드 파일들을 자동으로 감지
2.  **Lint 검사** - 각 언어별 린터를 사용한 코드 품질 검사
3.  **코드 실행** - 실제 코드를 실행하여 정상 작동 여부 확인
4.  **결과 리포트** - PR에 자동으로 검증 결과 코멘트 작성

-----

## 코드 리뷰어 자동 할당

CODEOWNERS 파일을 통해 언어별로 전문 리뷰 팀이 자동으로 할당됩니다:

* Python: `@techeer-sv/itddan-py-reviewers`
* Java: `@techeer-sv/itddan-java-reviewers`
* JavaScript: `@techeer-sv/itddan-js-reviewers`
* Go: `@techeer-sv/itddan-go-reviewers`

-----

## 로컬 개발 워크플로우

### 기본 사용법

1.  코딩 테스트 문제 해결 코드를 작성합니다.
2.  적절한 확장자(.py, .java, .js, .go)로 파일을 저장합니다.
3.  **로컬에서 린트 검사**를 실행합니다 (선택사항).
4.  Pull Request를 생성합니다.
5.  자동으로 린트 검사와 코드 실행이 수행됩니다.
6.  언어별 전문 리뷰어가 자동으로 할당됩니다.

### 로컬 린트 검사 (권장) 및 자동 수정

PR 생성 전에 로컬에서 미리 검사하거나 문제를 자동 수정해보세요. 자세한 설치 및 실행 방법은 각 언어별 **린팅 가이드** 문서를 참조해주세요.
