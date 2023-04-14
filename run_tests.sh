#!/bin/bash

export PATH=$PATH:/usr/bin:/bin

echo ''
echo "Running unit tests..."
cd src/relaunch/2023/tests//unit || exit
pytest --junit-xml=../test-results/junit.xml --verbose
#python -m unittest --verbose --buffer

echo ''
echo "Running functional tests..."
cd ../functional || exit
behavex -o ../test-results --logging-level WARNING --tags ~@manual

