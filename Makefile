BIN := venv/bin
PYTHON := $(BIN)/python

.PHONY: test
test: venv
	$(BIN)/py.test -v tests/
	$(BIN)/pre-commit run --all-files

venv: requirements.txt requirements-dev.txt
	uv venv venv -p python3.12
	uv pip install --python venv/bin/python -r requirements.txt -r requirements-dev.txt

.PHONY: install-hooks
install-hooks: venv
	$(BIN)/pre-commit install -f --install-hooks

.PHONY: clean
clean:
	rm -rf venv

.PHONY: update-requirements
update-requirements:
	uv pip compile requirements-minimal.txt -o requirements.txt
	uv pip compile requirements-dev-minimal.txt -o requirements-dev.txt
	sed -i 's/^ocflib==.*/ocflib/' requirements.txt
