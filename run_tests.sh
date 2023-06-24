#!/bin/bash

export PATH=$PATH:/usr/bin:/bin

echo ''
echo "Running unit tests..."
cd src/tests//unit || exit
pytest --junit-xml=../test-results/unit/junit.xml --verbose

echo ''
echo "Running functional tests..."
cd ../functional || exit
behavex -o ../test-results/functional --logging-level WARNING --tags ~@manual

