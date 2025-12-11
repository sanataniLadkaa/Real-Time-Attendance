#!/usr/bin/env bash
# sync_offline.sh - scans local cache and uploads to FastAPI endpoint
CACHE_DIR=${1:-"./offline_cache"}
BACKEND=${2:-"http://localhost:8000"}
for f in $(find "$CACHE_DIR" -type f); do
  ext="${f##*.}"
  if [[ "$ext" == "wav" ]]; then
    echo "Uploading audio $f"
    curl -F "file=@${f}" -F "employee_id=E100" "${BACKEND}/v1/voice/verify"
  elif [[ "$ext" == "jpg" || "$ext" == "png" ]]; then
    echo "Uploading image $f"
    curl -F "file=@${f}" -F "employee_id=E100" "${BACKEND}/v1/face/verify"
  fi
done
