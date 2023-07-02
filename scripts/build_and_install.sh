#!/bin/sh
VERSION_STR=$(python -m build)
FILE=$(echo $VERSION_STR | grep -oh -E '(jplaw-[0-9].[0-9].[0-9]).tar.gz')
echo "File is $FILE"
VERSION=$(echo $FILE | grep -oh -E '([0-9].[0-9].[0-9])')
echo "Version is $VERSION"
python -m pip install "dist/$FILE"
