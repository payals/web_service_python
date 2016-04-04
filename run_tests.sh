#!/usr/bin/bash

export PYTHONPATH=lib:server
echo "For tests to run properly, run it on port 8080 on localhost"
for i in test_fibonacci.py test_general.py ; do
	echo "running test: $i"
	python "tests/$i"
done
