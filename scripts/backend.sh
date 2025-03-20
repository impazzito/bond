#!/bin/bash

cd "$(dirname "${BASH_SOURCE[0]}")/../bond/frontend"

uv run                                       \
    --isolated                               \
    --with-requirements requirements.txt     \
    --python 3.13.2                          \
    --python-preference only-managed         \
    python -m bond "$@"