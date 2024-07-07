#!/bin/bash
import sys

from modelscope import snapshot_download


MODEL_NAME = sys.argv[1]
model_dir = snapshot_download(MODEL_NAME)

print(model_dir)
