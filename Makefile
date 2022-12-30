.PHONY: all prod dev format test lint type

all: format tests lint type

prod:
	@poetry install --without tests, docs

dev:
	@poetry install

format:
	@black .
	@isort .

test:
	@pytest .

lint:
	@flake8 .