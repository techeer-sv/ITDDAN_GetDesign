#!/bin/bash
# chmod +x lintfix.sh
# ./lintfix.sh
echo "🧹 Auto-fixing lint issues for all supported languages..."

# -----------------------------------------
# Python: black + isort
# -----------------------------------------
if command -v black &> /dev/null && command -v isort &> /dev/null; then
  echo "🐍 Fixing Python files with black and isort..."
  black .
  isort .
else
  echo "⚠️ Python tools (black, isort) not found. Skipping Python lint fix."
fi

# -----------------------------------------
# JavaScript: prettier + eslint --fix
# -----------------------------------------
if command -v prettier &> /dev/null && command -v eslint &> /dev/null; then
  echo "🚀 Fixing JavaScript files with prettier and eslint..."
  prettier --write .
  eslint . --fix || echo "⚠️ ESLint fix may need a valid eslint.config.js in root."
else
  echo "⚠️ JavaScript tools (prettier, eslint) not found. Skipping JS lint fix."
fi

# -----------------------------------------
# Go: gofmt
# -----------------------------------------
if command -v gofmt &> /dev/null; then
  echo "🐹 Fixing Go files with gofmt..."
  find . -name '*.go' -exec gofmt -w {} \;
else
  echo "⚠️ gofmt not found. Skipping Go lint fix."
fi

# -----------------------------------------
# Java: usually Checkstyle, but no auto-fix
# -----------------------------------------
echo "☕ Java (Checkstyle) does not support auto-fix. Please fix manually if issues exist."

echo "✅ All auto-fixable lint issues processed."
