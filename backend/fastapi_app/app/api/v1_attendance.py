# backend/fastapi_app/app/api/v1_attendance.py
from fastapi import APIRouter, UploadFile, File, Form
from app.services.supabase_client import SupabaseClient

router = APIRouter()
supabase = SupabaseClient()

@router.post("/2fa")
async def attendance_2fa(
    face: UploadFile = File(...),
    voice: UploadFile = File(...),
    employee_id: str = Form(...)
):
    # For week1, we accept both files and return mock combined verification
    face_contents = await face.read()
    voice_contents = await voice.read()
    if not face_contents or not voice_contents:
        return {"status": "error", "detail": "face and voice required"}
    return {"status": "ok", "result": {"employee_id": employee_id, "face_score": 0.82, "voice_score": 0.79, "verified": True}}
