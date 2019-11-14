help: ## Shows this help
	@echo "$$(grep -h '#\{2\}' $(MAKEFILE_LIST) | sed 's/: #\{2\} /	/' | column -t -s '	')"

install: ## Install requirements
	@[ -n "${VIRTUAL_ENV}" ] || (echo "ERROR: This should be run from a virtualenv" && exit 1)
	pip install -r requirements.txt

clean:
	rm -rf *.egg-info
	rm -rf dist
	find . -name ".DS_Store" -delete
	find . -name "__pycache__" -delete

build:
	flit build

tdd: ## Run test watcher
	nodemon -e py -x "python test_project_runpy.py --failfast"

test: ## Run test suite
	coverage erase
	coverage run test_project_runpy.py
	coverage report

# Bump project_runpy.__version__
# Update CHANGELOG (TODO)
# `git commit -am "1.0.0"`
# `make publish`
# `git tag v1.0.0`
# `git push --tags origin master`
publish: ## Publish a release to PyPI
	flit publish
