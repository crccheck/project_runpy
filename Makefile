help: ## Shows this help
	@echo "$$(grep -h '#\{2\}' $(MAKEFILE_LIST) | sed 's/: #\{2\} /	/' | column -t -s '	')"

clean:
	rm -rf *.egg-info
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

test: ## Run test suite
	python test_project_runpy.py

coverage:
	coverage erase
	coverage run test_project_runpy.py
	coverage report --show-missing

# remember you need `pip install wheel`
release:
	python setup.py sdist bdist_wheel upload
