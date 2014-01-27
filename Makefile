clean:
	rm -rf *.egg-info
	rm -rf .tox
	rm -rf build
	rm -rf dist
	rm -rf MANIFEST
	find . -name "*.pyc" -delete
	find . -name ".DS_Store" -delete
	find . -name "__pycache__" -delete

build:
	python setup.py sdist

all: clean build


test:
	nosetests

tox:
	tox


.PHONY: clean build all test tox
