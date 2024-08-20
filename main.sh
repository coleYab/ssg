#!/usr/bin/env bash
# running the main project
rm -rf public
mkdir public
python3 main.py
cd public
pwd
python3 -m http.server 8888
