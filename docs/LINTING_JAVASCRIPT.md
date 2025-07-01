## JavaScript 린팅 가이드

JavaScript 코드의 품질과 스타일을 일관되게 유지하기 위한 린터 및 포맷터 설정과 사용법을 안내합니다.

### 1. 도구 설치

```bash
npm install -g eslint prettier
````

> 참고: 현재 CI/CD 워크플로우는 전역 설치를 기준으로 동작합니다.

### 2. 명령어

작성한 코드를 검사하고 스타일을 통일하는 방법입니다.

#### 코드 검사

`eslint`와 `prettier`를 사용하여 코드의 문제점과 스타일 위반을 검사합니다.

```bash
# 린트 검사
eslint <파일 경로>

# 포맷팅 검사
prettier --check <파일 경로>
```

예시:

```bash
eslint fizzbuzz.js
prettier --check fizzbuzz.js
```

#### 자동 수정

수정 가능한 오류와 코드 스타일을 자동으로 수정합니다.

```bash
# 린트 자동 수정
eslint --fix <파일 경로>

# 자동 포맷팅
prettier --write <파일 경로>
```

예시:

```bash
eslint --fix fizzbuzz.js
prettier --write fizzbuzz.js
```
