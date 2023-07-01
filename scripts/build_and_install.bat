cd ..
py -m build
set /p VER=<VERSION
echo Version is %VER%
py -m pip install /dist/jplaw-%VER%.tar.gz