#!/usr/bin/env bash

# This script interpolates the html output of `markdown dieselrules.md` into a
# basic html skeleton and writes the whole thing to stdout

MARKDOWN_RULES="$(pwd)"/docs/dieselrules.md

if [[ -z "$(which markdown)" ]]; then
    echo "Please install markdown" >&2;
    exit 1;
elif [[ ! -e "$MARKDOWN_RULES" ]]; then
    echo "This script should be run from the project root" >&2;
    exit 1;
fi

BODY=$(markdown "$MARKDOWN_RULES" | tail -n +2)

HEADER=$(cat<<EOF
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Dieselrobin | Rules</title>
  <style>
    body {font-family: sans-serif;}
  </style>
</head>
<body>
<h1>Dieselrobin Rules</h1>
\n
EOF
);

FOOTER=$(cat<<EOF
</body>
</html>
EOF
);

echo -e "$HEADER" "$BODY" "$FOOTER"
