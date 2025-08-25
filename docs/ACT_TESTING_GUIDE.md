# Git Bash에서 Act로 GitHub Actions 로컬 테스트하기

## 개요

Act는 GitHub Actions를 로컬에서 실행할 수 있게 해주는 도구입니다. Git Bash 환경에서 act를 사용하여 워크플로우를 테스트하는 방법을 안내합니다.

## 사전 요구사항

### 1. Docker Desktop 설치

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) 다운로드 및 설치
- WSL2 지원 활성화 권장

### 2. Git Bash

- Git과 함께 설치된 Git Bash 사용

## Act 설치

### 방법 1: Homebrew 사용 (Mac OS)

```bash
# 최신 안정 릴리스 설치 (권장)
brew install act
# 가장 최신 개발 버전 설치
brew install act --HEAD
# 버전 조회
act --version
```

### 방법 2: Gihub CLI(Git bash) 사용 (Mac OS / Window) (권장)

```bash
# gh 확장으로 설치
gh extension install nektos/gh-act
# 버전 조회
gh act --version
```

## 파일 생성 후 Pull Request CI 테스트

```bash
git add *
git commit -m "새 파일 추가"
# bash에서
act pull_request
# git bash에서
gh act pull_request
```

## 기본 사용법 (git bash)

### 워크플로우 조회

```bash
gh act -l
```

### 워크플로우 테스트

```bash
# 모든 워크플로우 실행
gh act

# 특정 워크플로우 실행
gh act -W .github/workflows/specific-workflow.yml

# 특정 이벤트로 실행
gh act push
gh act pull_request
gh act workflow_dispatch

# 특정 job만 실행
gh act -j {jobID}
```

### 드라이 런 및 확인

```bash
# 워크플로우 구조 확인
gh act --list

# 드라이 런 (실제 실행하지 않음)
gh act --dryrun
```

## 문제 해결

### Docker 연결 문제

```bash
# Docker 상태 확인
docker info

# WSL2 재시작
wsl --shutdown
wsl
```

### 권한 문제

```bash
# Git Bash를 관리자 권한으로 실행
# 또는 Docker 그룹에 사용자 추가
```

### 경로 문제

```bash
# 현재 디렉토리 기준으로 설정
export ACT_STAGING=$(pwd)/act-staging
```

### 메모리 부족

```bash
# Docker Desktop > Settings > Resources > Memory: 4GB 이상 권장
```

### 로그 레벨 설정

```bash
# 상세한 로그
act --log-level debug

# 간단한 로그
act --log-level info
```

## 모범 사례

### 개발 워크플로우

- `act --dryrun`으로 먼저 구조 확인
- 작은 워크플로우부터 단계적으로 테스트
- WSL2 사용 시 Linux 컨테이너 활용

## 참고 자료

- [Act 공식 문서](https://nektosact.com/)
- [Act GitHub 저장소](https://github.com/nektos/act)
- [WSL2 설치 가이드](https://docs.microsoft.com/en-us/windows/wsl/install)
- [Git for Windows](https://gitforwindows.org/)

## 문제 보고

문제가 발생하면 다음 정보와 함께 이슈를 생성하세요:

- Act 버전: `act --version`
- Docker 버전: `docker --version`
- Git Bash 버전
- 에러 메시지 전체
- 워크플로우 파일 내용
