# test_and_commit.sh 실행 가이드

## 개요

Java 및 Python 코드 파일을 자동으로 스테이징하고 커밋한 후, GitHub Actions 테스트를 로컬에서 실행하는 자동화 스크립트입니다.

## 사전 요구사항

- **Git**: 버전 관리 시스템
- **GitHub CLI**: `gh` 명령어 사용
- **Act**: GitHub Actions 로컬 실행 도구

## Act 설치

- [Act 설치 가이드](../docs/ACT_TESTING_GUIDE.md#act-설치)

## 사용 방법

### 1. 실행 권한 부여 (Linux/macOS) (필요시)

```bash
chmod +x bin/test_and_commit.sh
```

### 2. 스크립트 실행 (git bash)

```bash
./bin/test_and_commit.sh
# 또는
bash bin/test_and_commit.sh
```

## 동작 과정

1. **파일 스테이징**: 수정된 `.java`, `.py` 파일 자동 추가
2. **자동 커밋**: `feat: 업데이트 Modified files: [파일목록]` 형식으로 커밋
3. **로컬 테스트**: `gh act push`로 GitHub Actions 워크플로우 실행
   - 성공 시: 성공 메시지 출력 "Automation script finished."
   - 실패 시: 커밋 자동 되돌림

## 주의사항

- git bash에서 실행 가능

## Act 가이드

- [Act 테스트 가이드](../docs/ACT_TESTING_GUIDE.md)
