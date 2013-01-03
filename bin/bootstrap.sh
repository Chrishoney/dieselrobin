#!/bin/bash

BOOTSTRAP_URL="http://twitter.github.com/bootstrap/assets/bootstrap.zip"
ARCHIVE="bootstrap.zip"
STATIC_DIR="static/"

wget --no-verbose $BOOTSTRAP_URL
unzip -q $ARCHIVE
mv $ARCHIVE $STATIC_DIR
