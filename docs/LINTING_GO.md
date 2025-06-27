## Go 린팅 가이드

Go 코드의 품질과 스타일을 일관되게 유지하기 위한 린터 및 포맷터 설정과 사용법을 안내합니다.

### 1. 도구 설치

```bash
go install github.com/golangci/golangci-lint/cmd/golangci-lint@latest
````

> `gofmt`는 Go 설치 시 기본적으로 포함되어 있습니다.

### 2. 명령어

작성한 코드를 검사하고 스타일을 통일하는 방법입니다.

#### 코드 검사

`gofmt`와 `golangci-lint`를 사용하여 코드 스타일과 잠재적인 오류를 검사합니다.

```bash
# 포맷팅 검사 (수정이 필요한 파일 목록 출력)
gofmt -l <파일 경로>

# 린트 검사
golangci-lint run <파일 경로>
```

예시:

```bash
gofmt -l ryan/week1/fizzbuzz.go
golangci-lint run ryan/week1/fizzbuzz.go
```

#### 자동 수정

`gofmt`를 사용하여 코드 스타일을 자동으로 수정합니다.

```bash
gofmt -w <파일 경로>
```

예시:

```bash
gofmt -w ryan/week1/fizzbuzz.go
```
