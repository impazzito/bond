#!/bin/bash

cd "$(dirname "${BASH_SOURCE[0]}")"

uv run --with grpcio-tools python3 -m grpc_tools.protoc types.proto     -I. \
    --python_out=. \
    --grpc_python_out=.