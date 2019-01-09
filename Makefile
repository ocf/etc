.PHONY: test
validate: *.yaml
	python3 validate.py

.PHONY: test
test:
	tox

.PHONY: clean
clean:
	rm -r .tox
