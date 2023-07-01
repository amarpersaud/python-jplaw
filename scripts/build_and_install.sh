#!/bin/sh
python -m build
VER=$(python setup.py --version)
python -m pip install "dist/jplaw-$VER.tar.gz"
