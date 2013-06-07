clean:
	find . -name "*.pyc" -delete
	find . -name ".DS_Store" -delete
	rm -rf .tox
	rm -rf MANIFEST
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info

build:
	python setup.py sdist

all: clean build


test:
	nosetests


.PHONY: clean test
