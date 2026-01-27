#!/usr/bin/env sh
set -euo pipefail

docker build -t ai-llm-reference-app:local .

docker run \
  --rm \
  -p 8000:8000 \
  --read-only \
  --tmpfs /tmp \
  ai-llm-reference-app:local
