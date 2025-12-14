# backend/fastapi_app/app/services/supabase_client.py
import os
from dotenv import load_dotenv
load_dotenv()

class SupabaseClient:
    def __init__(self):
        self.url = os.getenv("SUPABASE_URL")
        self.key = os.getenv("SUPABASE_SERVICE_KEY")

        if not self.url or not self.key:
            raise RuntimeError("SUPABASE_URL or SUPABASE_SERVICE_KEY not set")

        from supabase import create_client
        self.client = create_client(self.url, self.key)

    def upload_file(
        self,
        bucket: str,
        path: str,
        contents: bytes,
        content_type: str = "application/octet-stream",
    ):
        return self.client.storage.from_(bucket).upload(
            path, contents, content_type=content_type
        )


# ✅ THIS IS THE MISSING LINE
supabase = SupabaseClient()
