#!/bin/bash

cd "$(dirname "${BASH_SOURCE[0]}")"

uv run --with betterproto[compiler] --with grpcio-tools python3 -m grpc_tools.protoc -I . --python_betterproto_out=bond types.proto