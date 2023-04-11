#!/usr/bin/env bash

echo ''
echo "Running unit tests..."
cd src/relaunch/2023/tests//unit || exit
python -m unittest --verbose --buffer

echo ''
echo "Running functional tests..."
cd ../functional || exit
behavex -o ../test-results --logging-level WARNING --tags ~@manual

