BIN := .venv/bin
PYTHON := $(BIN)/python

.PHONY: test
test: .venv
	$(BIN)/py.test -v tests/
	$(BIN)/pre-commit run --all-files

.venv: pyproject.toml uv.lock
	uv sync --group dev

.PHONY: install-hooks
install-hooks: .venv
	$(BIN)/pre-commit install -f --install-hooks

.PHONY: clean
clean:
	rm -rf .venv

.PHONY: update-requirements
update-requirements:
	uv lock --upgrade
