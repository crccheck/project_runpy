help: ## Shows this help
	@echo "$$(grep -h '#\{2\}' $(MAKEFILE_LIST) | sed 's/: #\{2\} /	/' | column -t -s '	')"

install: ## Install requirements
	@[ -n "${VIRTUAL_ENV}" ] || (echo "ERROR: This should be run from a virtualenv" && exit 1)
	pip install -r requirements.txt

clean:
	rm -rf *.egg-info
	rm -rf dist
	rm -rf MANIFEST
	find . -name "*.pyc" -delete
	find . -name ".DS_Store" -delete
	find . -name "__pycache__" -delete

build:
	flit build

test: ## Run test suite
	coverage erase
	coverage run test_project_runpy.py
	coverage report

publish: ## Publish a release to PyPI
	flit publish
