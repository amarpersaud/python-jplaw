#!/bin/sh
python -m build
VER=$(python scripts/getversion.py)
python -m pip install "dist/jplaw-$VER.tar.gz"
