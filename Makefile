all: install format test build changelog

documentation:
	jb clean docs
	jb build docs

format:
	black . -l 79

install:
	pip install -e .[dev]

test:
	policyengine-core test policyengine_il/tests -c policyengine_il

build:
	python -m build

changelog:
	python .github/bump_version.py
	towncrier build --yes --version $$(python -c "import re; print(re.search(r'version = \"(.+?)\"', open('pyproject.toml').read()).group(1))")