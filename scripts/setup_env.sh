#!/usr/bin/env bash

. ~/LocalHooks/bin/activate

set -e
set -x

rm -f pep8.log pyflakes.log

./tests/test-subsequence.py

pep8 --max-line-length=120 ./subsequence.py > pep8.log || true
pyflakes ./subsequence.py pyflakes.log || true
