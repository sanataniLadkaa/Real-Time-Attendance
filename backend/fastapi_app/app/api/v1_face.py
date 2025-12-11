# backend/fastapi_app/app/api/v1_face.py
from fastapi import APIRouter, File, UploadFile, HTTPException, Depends
from typing import Dict
from app.services.supabase_client import SupabaseClient
from app.models.loader import ModelLoader

router = APIRouter()

# Dependency injection (simple)
supabase = SupabaseClient()
models = ModelLoader()

@router.post("/verify")
async def verify_face(file: UploadFile = File(...), employee_id: str = None):
    """
    Accepts an image file, runs face detection + embedding + verifies against stored embeddings.
    """
    # save temporary file
    contents = await file.read()
    if not contents:
        raise HTTPException(status_code=400, detail="Empty file")
    # For Week 1: mock embedding & verification flow
    # In Week 2 we'll replace with actual model inference.
    # TODO: run models.face_detector + models.face_embedding
    # Mock response:
    result = {"employee_id": employee_id, "score": 0.82, "verified": True}
    return {"status": "ok", "result": result}
