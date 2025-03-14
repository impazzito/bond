#!/bin/bash


cd "$(dirname "${BASH_SOURCE[0]}")/bond/frontend"

npm install
npm run "$@"
