# backend/fastapi_app/app/services/supabase_client.py
import os
from typing import Optional
import base64
from dotenv import load_dotenv
load_dotenv()

class SupabaseClient:
    def __init__(self):
        self.url = os.getenv("SUPABASE_URL")
        self.key = os.getenv("SUPABASE_SERVICE_KEY")
        # For Week 1 we use a minimal fetch approach via HTTP or supabase-py.
        try:
            from supabase import create_client
            self.client = create_client(self.url, self.key)
        except Exception:
            self.client = None

    def upload_file(self, bucket: str, path: str, contents: bytes, content_type: str = "application/octet-stream"):
        """
        Upload file to Supabase Storage. If client not available, raise informative error.
        """
        if not self.client:
            raise Exception("supabase client not available. Install supabase package and set SUPABASE_URL and SUPABASE_SERVICE_KEY")
        return self.client.storage.from_(bucket).upload(path, contents, content_type=content_type)

    # add more helpers as needed
