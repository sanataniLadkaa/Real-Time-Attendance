from app.models.voice_models import VoiceModel
from app.services.similarity import cosine_similarity

voice_model = VoiceModel()

def verify_voice(audio_path, stored_embeddings):
    emb = voice_model.extract_embedding(audio_path)
    scores = [cosine_similarity(emb, e) for e in stored_embeddings]
    return emb, max(scores)
