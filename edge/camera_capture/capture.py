# edge/camera_capture/capture.py
"""
Simple camera capture that takes a frame every N seconds, saves locally, optionally uploads to Supabase.
Usage: python capture.py --employee_id E123 --upload true
"""
import cv2
import argparse
import os
import time
from pathlib import Path
import base64
import requests

def capture_frame(save_path: str):
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise RuntimeError("Camera not accessible.")
    ret, frame = cap.read()
    cap.release()
    if not ret:
        raise RuntimeError("Failed to capture frame.")
    cv2.imwrite(save_path, frame)

def upload_to_backend(image_path: str, backend_url: str, employee_id: str):
    with open(image_path, "rb") as f:
        files = {"file": ("frame.jpg", f, "image/jpeg")}
        data = {"employee_id": employee_id}
        resp = requests.post(f"{backend_url}/v1/face/verify", files=files, data=data, timeout=15)
        print("Upload response:", resp.status_code, resp.text)
    return

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--employee_id", required=True)
    p.add_argument("--upload", default="false")
    p.add_argument("--backend_url", default="http://localhost:8000")
    p.add_argument("--out", default="captures")
    args = p.parse_args()

    outdir = Path(args.out)
    outdir.mkdir(parents=True, exist_ok=True)
    path = outdir / f"{args.employee_id}_{int(time.time())}.jpg"
    capture_frame(str(path))
    print(f"Saved frame to {path}")
    if args.upload.lower() in ("true", "1", "yes"):
        upload_to_backend(str(path), args.backend_url, args.employee_id)
