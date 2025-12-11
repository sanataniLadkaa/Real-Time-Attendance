# edge/audio/voice_capture.py
"""
Capture short audio from default microphone and save as WAV.
Requires: sounddevice, soundfile
Usage: python voice_capture.py --duration 3 --employee_id E123 --upload true
"""
import argparse
import sounddevice as sd
import soundfile as sf
from pathlib import Path
import time
import requests

def record_to_file(path: str, duration: float = 3.0, samplerate: int = 16000):
    print("Recording...")
    data = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='int16')
    sd.wait()
    sf.write(path, data, samplerate)
    print("Saved audio to", path)

def upload_audio(path: str, backend_url: str, employee_id: str):
    with open(path, "rb") as f:
        files = {"file": ("rec.wav", f, "audio/wav")}
        data = {"employee_id": employee_id}
        resp = requests.post(f"{backend_url}/v1/voice/verify", files=files, data=data, timeout=20)
        print("Upload response:", resp.status_code, resp.text)

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--duration", type=float, default=3.0)
    p.add_argument("--employee_id", required=True)
    p.add_argument("--upload", default="false")
    p.add_argument("--backend_url", default="http://localhost:8000")
    p.add_argument("--out", default="captures_audio")
    args = p.parse_args()

    outdir = Path(args.out)
    outdir.mkdir(parents=True, exist_ok=True)
    path = outdir / f"{args.employee_id}_{int(time.time())}.wav"
    record_to_file(str(path), args.duration)
    if args.upload.lower() in ("true","1","yes"):
        upload_audio(str(path), args.backend_url, args.employee_id)
