# backend/fastapi_app/app/api/v1_voice.py
from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.supabase_client import SupabaseClient

router = APIRouter()
supabase = SupabaseClient()

@router.post("/verify")
async def verify_voice(file: UploadFile = File(...), employee_id: str = None):
    contents = await file.read()
    if not contents:
        raise HTTPException(status_code=400, detail="Empty audio")
    # Week 1: mock response
    return {"status": "ok", "result": {"employee_id": employee_id, "score": 0.78, "verified": True}}
