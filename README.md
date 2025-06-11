# ITDDAN_GetDesign
We build things

## 🚀 지원 언어 및 도구

이 프로젝트는 코딩 테스트 문제 해결을 위한 다양한 언어를 지원하며, 각 언어별로 자동화된 코드 품질 검사를 제공합니다.

### 📋 지원 언어
- 🐍 **Python** (.py)
- ☕ **Java** (.java)  
- 🚀 **JavaScript** (.js)
- 🐹 **Go** (.go)

### 🧹 코드 품질 도구 (Linters)

#### 🐍 Python
**설치:**
```bash
pip install black isort flake8
```

**개별 실행:**
```bash
black --check --diff your_file.py
isort --check-only --diff your_file.py
flake8 your_file.py --max-line-length=88
```

**🚀 통합 스크립트 사용 (권장):**
```bash
# 어디서든 쉽게 실행 (프로젝트 루트에서)
./lint-python two_sum.py              # 특정 파일 린트
./lint-python                         # 모든 Python 파일 린트

# 또는 원본 스크립트 직접 실행
./scripts/lint_python.sh two_sum.py   # 특정 파일 린트
./scripts/lint_python.sh              # 모든 Python 파일 린트
```

**💡 개선된 경로 처리:**
- 스크립트가 자동으로 프로젝트 루트를 찾아서 실행됩니다
- 어떤 디렉토리에서든 상대/절대 경로 상관없이 동작합니다
- `../../../some_file.py` 같은 복잡한 경로가 필요 없습니다!

**도구:**
- **[Black](https://black.readthedocs.io/)** - 코드 포맷터
- **[isort](https://pycqa.github.io/isort/)** - import 정렬 도구
- **[flake8](https://flake8.pycqa.org/)** - 스타일 가이드 및 에러 체크

#### 🚀 JavaScript
**설치:**
```bash
npm install -g eslint prettier
```

**실행:**
```bash
eslint your_file.js
prettier --check your_file.js
```

**도구:**
- **[ESLint](https://eslint.org/)** - 코드 품질 및 스타일 검사
- **[Prettier](https://prettier.io/)** - 코드 포맷터

#### ☕ Java
**설치:**
```bash
# Checkstyle JAR 다운로드
wget https://github.com/checkstyle/checkstyle/releases/download/checkstyle-10.12.4/checkstyle-10.12.4-all.jar
```

**실행:**
```bash
java -jar checkstyle-10.12.4-all.jar -c checkstyle.xml YourFile.java
```

**도구:**
- **[Checkstyle](https://checkstyle.sourceforge.io/)** - 코딩 스타일 및 규칙 검사

#### 🐹 Go
**설치:**
```bash
# gofmt는 Go 설치시 기본 포함
# golangci-lint 설치
go install github.com/golangci/golangci-lint/cmd/golangci-lint@latest
```

**실행:**
```bash
gofmt -l your_file.go
golangci-lint run your_file.go
```

**도구:**
- **[gofmt](https://golang.org/cmd/gofmt/)** - Go 표준 포맷터
- **[golangci-lint](https://golangci-lint.run/)** - 통합 Go 린터

## 🔄 CI/CD 워크플로우

GitHub Actions를 통해 자동으로 다음 작업들이 수행됩니다:

1. **🔍 파일 변경 감지** - 수정된 코드 파일들을 자동으로 감지
2. **🧹 Lint 검사** - 각 언어별 린터를 사용한 코드 품질 검사
3. **🧪 코드 실행** - 실제 코드를 실행하여 정상 작동 여부 확인
4. **📝 결과 리포트** - PR에 자동으로 검증 결과 코멘트 작성

## 🏷️ 코드 리뷰어 자동 할당

CODEOWNERS 파일을 통해 언어별로 전문 리뷰어가 자동으로 할당됩니다:

- 🐍 Python: `@ITDDAN-py-reviewer`
- ☕ Java: `@ITDDAN-java-reviewer`
- 🚀 JavaScript: `@ITDDAN-js-reviewer`
- 🐹 Go: `@ITDDAN-go-reviewer`

## 🔧 로컬 개발 워크플로우

### 📝 기본 사용법
1. 코딩 테스트 문제 해결 코드를 작성합니다
2. 적절한 확장자(.py, .java, .js, .go)로 파일을 저장합니다
3. **로컬에서 린트 검사**를 실행합니다 (선택사항)
4. Pull Request를 생성합니다
5. 자동으로 린트 검사와 코드 실행이 수행됩니다
6. 언어별 전문 리뷰어가 자동으로 할당됩니다

### 🔍 로컬 린트 검사 (권장)
PR 생성 전에 로컬에서 미리 검사해보세요:

```bash
# Python (통합 스크립트 사용)
./lint-python your_file.py

# JavaScript
eslint your_file.js
prettier --check your_file.js

# Java
java -jar checkstyle.jar -c checkstyle.xml YourFile.java

# Go
gofmt -l your_file.go
golangci-lint run your_file.go
```

### 🛠️ 자동 수정 (Auto-fix)
린트 문제를 자동으로 수정하려면:

```bash
# Python
black your_file.py          # 포맷팅 자동 수정
isort your_file.py          # import 정렬 자동 수정

# JavaScript
prettier --write your_file.js    # 포맷팅 자동 수정
eslint --fix your_file.js        # 일부 문제 자동 수정

# Go
gofmt -w your_file.go            # 포맷팅 자동 수정
```

### ⚡ 빠른 시작 가이드

1. **린터 설치:**
   ```bash
   # Python
   pip install black isort flake8
   
   # JavaScript
   npm install -g eslint prettier
   
   # Go
   go install github.com/golangci/golangci-lint/cmd/golangci-lint@latest
   ```

2. **코드 작성 → 린트 검사 → 자동 수정 → 커밋**
   ```bash
   # 예시: Python 파일
   ./lint-python my_solution.py            # 검사
   black my_solution.py                     # 포맷팅 수정
   isort my_solution.py                     # import 정렬
   git add my_solution.py && git commit -m "Add solution"
   ```
