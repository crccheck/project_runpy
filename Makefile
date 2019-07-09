help: ## Shows this help
	@echo "$$(grep -h '#\{2\}' $(MAKEFILE_LIST) | sed 's/: #\{2\} /	/' | column -t -s '	')"

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
	python test_project_runpy.py

coverage:
	coverage erase
	coverage run test_project_runpy.py
	coverage report --show-missing

publish: ## Publish a release to PyPI
	flit publish
