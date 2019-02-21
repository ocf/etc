BIN := venv/bin
PYTHON := $(BIN)/python

.PHONY: test
test: venv
	$(BIN)/py.test -v tests/
	$(BIN)/pre-commit run --all-files

venv: requirements.txt
	python ./vendor/venv-update venv= venv -ppython3 install= -r requirements.txt -r requirements-dev.txt

.PHONY: install-hooks
install-hooks: venv
	$(BIN)/pre-commit install -f --install-hooks

.PHONY: clean
clean:
	rm -rf venv

.PHONY: update-requirements
update-requirements: venv
	$(BIN)/upgrade-requirements
	sed -i 's/^ocflib==.*/ocflib/' requirements.txt
