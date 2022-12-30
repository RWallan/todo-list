.PHONY: all prod dev format test lint type

all: format test lint type

prod:
	@poetry install --without tests, docs

dev:
	@poetry install

format:
	@black .
	@isort .

test:
	@pytest -v .

lint:
	@flake8 --exclude=.venv .