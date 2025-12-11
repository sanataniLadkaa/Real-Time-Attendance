# edge/inference/run_inference.py
"""
Mock inference runner that loads a local .engine (if present), otherwise returns a stub.
Real code on Jetson will use TensorRT Python bindings to run inference.
"""
import argparse
from pathlib import Path
import numpy as np

def run(image_path: str, engine_path: str = None):
    # stub: generate a deterministic pseudo-embedding from the image filename hash
    h = hash(Path(image_path).name)
    emb = np.array([(h >> i) & 255 for i in range(0, 512)])[:512].astype(float)
    # normalize
    emb = emb / (np.linalg.norm(emb) + 1e-9)
    return emb.tolist()

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--image")
    p.add_argument("--engine", default=None)
    args = p.parse_args()
    embedding = run(args.image, args.engine)
    print("embedding len:", len(embedding))
