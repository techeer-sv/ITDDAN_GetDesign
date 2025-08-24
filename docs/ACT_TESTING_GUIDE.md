# Act를 사용한 GitHub Actions 로컬 테스트 가이드

## 개요

Act는 GitHub Actions를 로컬에서 실행할 수 있게 해주는 도구입니다. Windows와 macOS 환경에서 act를 사용하여 워크플로우를 테스트하는 방법을 안내합니다.

## 사전 요구사항

### 1. Docker Desktop 설치

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) 다운로드 및 설치
- **Windows**: WSL2 지원 활성화 권장
- **macOS**: Apple Silicon(M1/M2) 또는 Intel 프로세서에 맞는 버전 설치

### 2. 터미널 환경

- **Git Bash 권장**:

## Act 설치

### Git bash에서 Act 설치

```bash
# 기본 실행 (모든 워크플로우)
gh extension install nektos/gh-act
```

설치 후 gh 명령을 통해 act 호출

```bash
gh act          # 단순히 'act' 대신
gh act -l
```

## 기본 사용법

### 1. 워크플로우 테스트

```bash
# 기본 실행 (모든 워크플로우)
act

# 특정 워크플로우 실행
act -W .github/workflows/specific-workflow.yml

# 특정 이벤트 트리거
act push
act pull_request
act workflow_dispatch
```

### 2. 드라이 런 (실제 실행하지 않고 확인)

```bash
# 워크플로우 구조 확인
act --list

# 드라이 런 (실제 실행하지 않음)
act --dryrun
```

### 3. 특정 Job 실행

```bash
# 특정 job만 실행
act -j build
act -j test
```

## 환경 설정

### 1. 환경 변수 설정

#### Windows (Git Bash)

```bash
# .bashrc 또는 .bash_profile에 추가
export ACT_LOG_LEVEL=debug
export ACT_STAGING=/c/act-staging

# Windows 경로를 Unix 경로로 변환
export ACT_STAGING=$(pwd)/act-staging
```

#### macOS

```bash
# .zshrc 또는 .bash_profile에 추가
export ACT_LOG_LEVEL=debug
export ACT_STAGING=$HOME/act-staging

# 또는 현재 디렉토리 기준
export ACT_STAGING=$(pwd)/act-staging
```

### 2. Docker 경로 설정

#### Windows

```bash
# Docker Desktop 경로 확인
export DOCKER_HOST="tcp://localhost:2375"

# 또는 WSL2 환경에서
export DOCKER_HOST="unix:///var/run/docker.sock"
```

#### macOS

```bash
# Docker Desktop 기본 설정 (일반적으로 설정 불필요)
# Docker Desktop이 실행 중인지 확인
docker info

# 필요시 수동 설정
export DOCKER_HOST="unix:///var/run/docker.sock"
```

## 일반적인 워크플로우 예제

### 1. Python 프로젝트 테스트

```yaml
# .github/workflows/test.yml
name: Python Tests
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.9"
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      - name: Run tests
        run: |
          python -m pytest
```

### 2. Java 프로젝트 테스트

```yaml
# .github/workflows/java.yml
name: Java CI
on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up JDK
        uses: actions/setup-java@v3
        with:
          java-version: "11"
          distribution: "temurin"
      - name: Build with Maven
        run: mvn clean compile test
```

## 문제 해결

### 1. Docker 연결 문제

#### Windows

```bash
# Docker 서비스 상태 확인
docker info

# Docker Desktop 재시작
# 또는 WSL2 재시작
wsl --shutdown
wsl
```

#### macOS

```bash
# Docker 서비스 상태 확인
docker info

# Docker Desktop 재시작
# 또는 터미널에서 Docker 재시작
osascript -e 'quit app "Docker"'
open -a Docker
```

### 2. 권한 문제

#### Windows

```bash
# Git Bash를 관리자 권한으로 실행
# 또는 Docker 그룹에 사용자 추가
```

#### macOS

```bash
# Docker 그룹에 사용자 추가 (필요시)
sudo usermod -aG docker $USER

# 실행 권한 확인
ls -la $(which act)
chmod +x $(which act)
```

### 3. 경로 문제

#### Windows

```bash
# Windows 경로를 Unix 경로로 변환
export ACT_STAGING=$(pwd)/act-staging

# 또는 절대 경로 사용
export ACT_STAGING="/c/Users/username/act-staging"
```

#### macOS

```bash
# Unix 경로 사용
export ACT_STAGING=$(pwd)/act-staging

# 또는 홈 디렉토리 기준
export ACT_STAGING="$HOME/act-staging"
```

### 4. 메모리 부족

#### Windows

```bash
# Docker Desktop 메모리 제한 증가
# Docker Desktop > Settings > Resources > Memory: 4GB 이상 권장
```

#### macOS

```bash
# Docker Desktop 메모리 제한 증가
# Docker Desktop > Settings > Resources > Memory: 4GB 이상 권장
# Apple Silicon Mac의 경우 6GB 이상 권장
```

## 고급 설정

### 1. 커스텀 이미지 사용

```bash
# 특정 이미지 사용
act -P ubuntu-latest=nektos/act-environments-ubuntu:18.04

# 로컬 이미지 사용
act -P ubuntu-latest=my-custom-image:latest
```

### 2. 시크릿 및 환경 변수

```bash
# 시크릿 파일 생성
echo "MY_SECRET=value" > .secrets

# 환경 변수 파일 생성
echo "NODE_ENV=test" > .env

# 실행 시 적용
act --secret-file .secrets --env-file .env
```

### 3. 로그 레벨 설정

```bash
# 상세한 로그
act --log-level debug

# 간단한 로그
act --log-level info
```

## 모범 사례

### 1. 개발 워크플로우

- `act --dryrun`으로 먼저 구조 확인
- 작은 워크플로우부터 단계적으로 테스트
- 로컬 환경과 GitHub 환경의 차이점 인지

### 2. 성능 최적화

- 필요한 job만 선택적으로 실행
- Docker 이미지 캐싱 활용
- 불필요한 단계 제거

### 3. 디버깅

- `--verbose` 플래그 사용
- 로그 레벨 조정
- 단계별 실행 및 검증

### 4. 플랫폼별 최적화

#### Windows

- WSL2 사용 시 Linux 컨테이너 활용
- Git Bash에서 Unix 명령어 사용

#### macOS

- Apple Silicon Mac의 경우 ARM64 이미지 우선 사용
- Intel Mac의 경우 x86_64 이미지 사용

## 유용한 명령어 모음

```bash
# 도움말
act --help

# 버전 확인
act --version

# 워크플로우 목록
act --list

# 특정 이벤트로 실행
act push
act pull_request
act workflow_dispatch

# 특정 job 실행
act -j build

# 드라이 런
act --dryrun

# 상세 로그
act --verbose

# 특정 워크플로우 파일 사용
act -W .github/workflows/custom.yml
```

## 참고 자료

- [Act 공식 문서](https://nektosact.com/)
- [Act GitHub 저장소](https://github.com/nektos/act)
- [GitHub Actions 공식 문서](https://docs.github.com/en/actions)
- [Docker Desktop 문서](https://docs.docker.com/desktop/)

### 플랫폼별 추가 자료

#### Windows

- [WSL2 설치 가이드](https://docs.microsoft.com/en-us/windows/wsl/install)
- [Git for Windows](https://gitforwindows.org/)

#### macOS

- [Homebrew 설치 가이드](https://brew.sh/)
- [Apple Silicon Mac 개발 환경 설정](https://developer.apple.com/documentation/xcode/developing-for-apple-silicon)

## 문제 보고

문제가 발생하면 다음 정보와 함께 이슈를 생성하세요:

- Act 버전: `act --version`
- Docker 버전: `docker --version`
- 운영체제 정보 및 아키텍처 (Windows x64, macOS ARM64/Intel)
- 터미널 환경 (Git Bash, PowerShell, Terminal.app, iTerm2)
- 에러 메시지 전체
- 워크플로우 파일 내용
- Docker Desktop 설정 정보
