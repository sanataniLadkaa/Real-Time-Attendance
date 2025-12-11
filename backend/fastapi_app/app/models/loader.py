# backend/fastapi_app/app/models/loader.py
import os
from typing import Any

class ModelLoader:
    """
    Simple model loader skeleton. Real models will be loaded and cached here (TensorRT on Jetson).
    """
    def __init__(self):
        self.models = {}

    def load(self, name: str) -> Any:
        # For week1, return a stub
        if name in self.models:
            return self.models[name]
        # Placeholder: load logic for TRT or Torch
        self.models[name] = {"name": name, "version": "week1-stub"}
        return self.models[name]
