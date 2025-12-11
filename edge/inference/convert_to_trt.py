# edge/inference/convert_to_trt.py
"""
Convert an ONNX/Torch model to TensorRT using trtexec or Python TensorRT builder.
This script provides commands and a simple wrapper; run on Jetson with TensorRT installed.
"""
import os
import argparse
import subprocess

def convert_with_trtexec(onnx_path: str, output_engine: str, fp16: bool = True):
    cmd = [
        "trtexec",
        f"--onnx={onnx_path}",
        f"--saveEngine={output_engine}",
        "--workspace=2048"
    ]
    if fp16:
        cmd.append("--fp16")
    print("Running:", " ".join(cmd))
    subprocess.check_call(cmd)

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--onnx", required=True)
    p.add_argument("--out", required=True)
    p.add_argument("--fp16", action="store_true")
    args = p.parse_args()
    convert_with_trtexec(args.onnx, args.out, args.fp16)
