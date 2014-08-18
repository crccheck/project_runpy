clean:
	rm -rf *.egg-info
	rm -rf .tox
	rm -rf build
	rm -rf dist
	rm -rf MANIFEST
	find . -name "*.pyc" -delete
	find . -name ".DS_Store" -delete
	find . -name "__pycache__" -delete

.PHONY: build
build:
	python setup.py sdist bdist_wheel

all: clean build

test:
	python tests.py

tox:
	tox

coverage:
	coverage erase
	coverage run tests.py
	coverage report --show-missing

# remember you need `pip install wheel`
release:
	python setup.py sdist bdist_wheel upload
