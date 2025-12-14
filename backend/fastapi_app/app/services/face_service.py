from app.models.face_models import FaceModel
from app.services.similarity import cosine_similarity
from app.services.supabase_client import supabase

face_model = FaceModel()

def verify_face(image_bytes):
    emb = face_model.extract_embedding(image_bytes)
    if emb is None:
        return None, 0.0, False

    # Fetch embeddings WITH employee_id
    rows = supabase.table("face_embeddings").select(
        "employee_id, embedding"
    ).execute().data

    best_score = 0.0
    best_employee = None

    for row in rows:
        score = cosine_similarity(emb, row["embedding"])
        if score > best_score:
            best_score = score
            best_employee = row["employee_id"]

    verified = best_score >= 0.75
    return best_employee, best_score, verified
