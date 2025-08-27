#!/bin/bash

# Java 및 Python 파일만 찾아서 Staging Area에 추가
echo "Adding Java and Python code files to the staging area..."
git ls-files -m -o --exclude-standard | grep -E '\.(java|py)$' | xargs git add

# 수정된 파일 목록을 변수에 저장
# `awk '{print $2}'`를 사용해 파일명만 추출합니다.
MODIFIED_FILES=$(git status -s | awk '{print $2}')

COMMIT_MESSAGE="feat: 업데이트 Modified files: ${MODIFIED_FILES}"
echo "Creating a new commit with message: '$COMMIT_MESSAGE'..."
git commit -m "$COMMIT_MESSAGE"

# 'push' 이벤트로 로컬에서 GitHub Actions 테스트
echo "Running GitHub Actions tests locally using 'act'..."
if gh act push; then
    echo "Tests passed successfully!"
    
else
    echo "Tests failed. Please check the workflow errors."
    
    # 실패한 경우 커밋 되돌리기
    git reset HEAD~1
    echo "Last commit has been reverted."
    exit 1
fi

echo "Automation script finished."
