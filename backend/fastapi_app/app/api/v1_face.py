# backend/fastapi_app/app/api/v1_face.py
from fastapi import APIRouter, File, UploadFile, HTTPException, Depends
from typing import Dict
from app.services.supabase_client import SupabaseClient
from app.models.loader import ModelLoader

router = APIRouter()

# Dependency injection (simple)
supabase = SupabaseClient()
models = ModelLoader()

from fastapi import APIRouter, UploadFile, File
from app.services.face_service import verify_face

router = APIRouter()

@router.post("/verify")
async def face_verify(file: UploadFile = File(...)):
    image_bytes = await file.read()

    employee_id, score, verified = verify_face(image_bytes)

    return {
        "status": "ok",
        "result": {
            "employee_id": employee_id,
            "score": round(score, 3),
            "verified": verified
        }
    }

