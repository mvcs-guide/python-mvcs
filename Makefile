.PHONY: test
test: clean lint
	@py.test -s samantha/tests

.PHONY: lint
lint:
	@flake8 samantha

.PHONY: clean
clean:
	@find . -type f -name '*.pyc' -exec rm {} ';'
