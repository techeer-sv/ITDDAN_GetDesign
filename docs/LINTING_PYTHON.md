## Python 린팅 가이드

Python 코드의 품질과 스타일을 일관되게 유지하기 위한 린터 및 코드 포맷터 설정과 사용법을 안내합니다.

### 1. 도구 설치

```bash
pip install black isort flake8
````

### 2. 명령어

작성한 코드를 검사하고 스타일을 통일하는 방법입니다.

#### 코드 검사

`lint_python.sh` 스크립트를 사용하여 코드 품질을 검사합니다.

```bash
./scripts/lint_python.sh <파일 경로>
```

예시:

```bash
./scripts/lint_python.sh fizzbuzz.py
```

#### 자동 수정

`black`과 `isort`를 사용하여 코드 스타일과 import 순서를 자동으로 수정합니다.

```bash
black <파일 경로>
isort <파일 경로>
```

예시:

```bash
black fizzbuzz.py
isort fizzbuzz.py
```
