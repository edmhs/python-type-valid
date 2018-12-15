
coverage: ## check code coverage quickly with the default Python
	#coverage run --source=tests/ test
	coverage report -m
	coverage html
	$(BROWSER) htmlcov/index.html

test:
	python -m unittest -v

lint:
	pycodestyle type_valid tests

clean:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr coverage/
	rm -fr .pytest_cache

dist: clean
	python setup.py sdist bdist_wheel
	twine upload --repository-url https://upload.pypi.org/legacy/ ./dist/*