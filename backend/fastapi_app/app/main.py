# backend/fastapi_app/app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import v1_face, v1_voice, v1_attendance

app = FastAPI(title="Attendance Inference API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(v1_face.router, prefix="/v1/face", tags=["face"])
app.include_router(v1_voice.router, prefix="/v1/voice", tags=["voice"])
app.include_router(v1_attendance.router, prefix="/v1/attendance", tags=["attendance"])

@app.get("/")
async def health():
    return {"status": "ok", "service": "attendance-inference"}
