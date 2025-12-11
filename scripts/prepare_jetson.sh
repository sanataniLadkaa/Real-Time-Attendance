#!/usr/bin/env bash
set -e
echo "Prepare Jetson: ensure TensorRT and trtexec are installed (JetPack)."
echo "To convert ONNX to TensorRT (example):"
echo "    trtexec --onnx=model.onnx --saveEngine=model.engine --fp16 --workspace=2048"
echo "See edge/inference/convert_to_trt.py for a wrapper."
