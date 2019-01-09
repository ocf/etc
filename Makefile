BIN := venv/bin
PYTHON := $(BIN)/python

.PHONY: .validate
validate: venv
	$(PYTHON) validate.py

venv: requirements.txt
	python ./vendor/venv-update venv= venv -ppython3 install= -r requirements.txt

.PHONY: install-hooks
install-hooks: venv
	$(BIN)/pre-commit install -f --install-hooks

.PHONY: lint
lint: venv
	$(BIN)/pre-commit run --all-files

.PHONY: clean
clean:
	rm -rf venv

.PHONY: update-requirements
update-requirements: venv
	$(BIN)/upgrade-requirements
	sed -i 's/^ocflib==.*/ocflib/' requirements.txt
