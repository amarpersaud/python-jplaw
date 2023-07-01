#!/bin/sh
cd ..
python3 -m build
VER=`cat VERSION`
python3 -m pip install "dist/jplaw-$VER.tar.gz"
