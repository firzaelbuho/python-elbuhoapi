# Makefile
start:
	uvicorn app.main:app

build:
	python -m build

dev:
	uvicorn app.main:app  --port 9000

test:
	pytest
