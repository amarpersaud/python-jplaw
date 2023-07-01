#!/bin/sh
VER=$(python setup.py --version)
python -m pdoc --html -o ./docs/v$VER jplaw
