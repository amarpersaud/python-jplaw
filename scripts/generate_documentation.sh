#!/bin/sh
VER=$(python setup.py --version)
rm -rf docs/v$VER
python -m pdoc --html -o ./docs/v$VER jplaw
mv docs/v$VER/jplaw/* docs/v$VER/
rm -rf docs/v$VER/jplaw/