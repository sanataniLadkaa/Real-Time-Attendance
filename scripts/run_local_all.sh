#!/usr/bin/env bash
# Run local stack: start fastapi and run example capture (assumes python env)
set -e
echo "Starting FastAPI (uvicorn)..."
pushd backend/fastapi_app
# run in background
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload &
UVC_PID=$!
sleep 2
popd
echo "Running a quick camera capture (mock; may fail if no camera)."
python3 edge/camera_capture/capture.py --employee_id E100 --upload false || true
echo "To stop FastAPI: kill $UVC_PID"
