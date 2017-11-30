# Makefile for Evolutionary Redcode Warriors.

init:
	pip3 install -r requirements.txt --user

run:
	@ python3 -m evored.main

test:
	nose2 tests
