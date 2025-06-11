#!/bin/bash

# 🐍 Python Linting Script
# Black, isort, flake8를 한 번에 실행하는 스크립트

set -e

# 프로젝트 루트 찾기 (.git 폴더가 있는 곳)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT=""

# 현재 스크립트 위치에서 시작해서 상위로 올라가며 .git 폴더 찾기
CURRENT_DIR="$SCRIPT_DIR"
while [ "$CURRENT_DIR" != "/" ]; do
    if [ -d "$CURRENT_DIR/.git" ]; then
        PROJECT_ROOT="$CURRENT_DIR"
        break
    fi
    CURRENT_DIR="$(dirname "$CURRENT_DIR")"
done

# .git 폴더를 찾지 못했으면 스크립트 위치의 상위 디렉토리를 사용
if [ -z "$PROJECT_ROOT" ]; then
    PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
fi

# 프로젝트 루트로 이동
cd "$PROJECT_ROOT"

echo "🐍 Python Linting Script Started"
echo "================================="
echo "📍 Project root: $PROJECT_ROOT"
echo "📍 Working directory: $(pwd)"

# 파라미터로 파일이 주어지지 않으면 모든 .py 파일 검사
if [ $# -eq 0 ]; then
    echo "📁 Searching for Python files..."
    FILES=$(find . -name "*.py" -not -path "./.git/*" -not -path "./venv/*" -not -path "./.venv/*" -not -path "./scripts/*")
    if [ -z "$FILES" ]; then
        echo "❌ No Python files found"
        exit 0
    fi
else
    # 파라미터로 받은 파일들의 경로 정규화
    FILES=""
    for arg in "$@"; do
        # 절대 경로인지 확인
        if [[ "$arg" = /* ]]; then
            # 절대 경로를 프로젝트 루트 기준 상대 경로로 변환
            REL_PATH=$(realpath --relative-to="$PROJECT_ROOT" "$arg" 2>/dev/null || echo "$arg")
        else
            # 이미 상대 경로인 경우, 현재 작업 디렉토리에서 프로젝트 루트로 변환
            if [ -f "$arg" ]; then
                REL_PATH="$arg"
            elif [ -f "$OLDPWD/$arg" ]; then
                REL_PATH=$(realpath --relative-to="$PROJECT_ROOT" "$OLDPWD/$arg" 2>/dev/null || echo "$arg")
            else
                REL_PATH="$arg"
            fi
        fi
        
        if [ -z "$FILES" ]; then
            FILES="$REL_PATH"
        else
            FILES="$FILES $REL_PATH"
        fi
    done
fi

echo "📋 Files to lint:"
for file in $FILES; do
    echo "  - $file"
done
echo ""

# 결과 추적 변수
TOTAL_FILES=0
PASSED_FILES=0
FAILED_FILES=""

# 각 파일에 대해 린팅 실행
for file in $FILES; do
    if [ ! -f "$file" ]; then
        echo "⚠️  Skipping $file (file not found)"
        continue
    fi
    
    echo "🔍 Linting: $file"
    TOTAL_FILES=$((TOTAL_FILES + 1))
    FILE_PASSED=true
    
    # 1. Black (포맷터 체크)
    echo "  🖤 Running Black..."
    if black --check --diff "$file" 2>/dev/null; then
        echo "  ✅ Black: PASSED"
    else
        echo "  ❌ Black: FAILED (formatting issues)"
        FILE_PASSED=false
    fi
    
    # 2. isort (import 정렬)
    echo "  📚 Running isort..."
    if isort --check-only --diff "$file" 2>/dev/null; then
        echo "  ✅ isort: PASSED"
    else
        echo "  ❌ isort: FAILED (import sorting issues)"
        FILE_PASSED=false
    fi
    
    # 3. flake8 (스타일 & 에러 체크)
    echo "  📏 Running flake8..."
    if flake8 "$file" --max-line-length=88 --ignore=E203,W503 2>/dev/null; then
        echo "  ✅ flake8: PASSED"
    else
        echo "  ❌ flake8: FAILED (style/error issues)"
        FILE_PASSED=false
    fi
    
    # 결과 집계
    if $FILE_PASSED; then
        echo "  🎉 $file: ALL CHECKS PASSED"
        PASSED_FILES=$((PASSED_FILES + 1))
    else
        echo "  💥 $file: SOME CHECKS FAILED"
        if [ -z "$FAILED_FILES" ]; then
            FAILED_FILES="$file"
        else
            FAILED_FILES="$FAILED_FILES, $file"
        fi
    fi
    echo ""
done

# 최종 결과 출력
echo "================================="
echo "🏁 FINAL RESULTS"
echo "================================="
echo "📊 Total files checked: $TOTAL_FILES"
echo "✅ Files passed: $PASSED_FILES"
echo "❌ Files failed: $((TOTAL_FILES - PASSED_FILES))"

if [ $PASSED_FILES -eq $TOTAL_FILES ]; then
    echo ""
    echo "🎉 SUCCESS: All Python files passed linting!"
    echo "🚀 Your code is ready for commit!"
    exit 0
else
    echo ""
    echo "💥 FAILED: Some files have linting issues"
    echo "📝 Files with issues: $FAILED_FILES"
    echo ""
    echo "🔧 Quick fixes:"
    echo "  - Run 'black .' to auto-format code"
    echo "  - Run 'isort .' to sort imports"
    echo "  - Check flake8 output for specific issues"
    exit 1
fi 