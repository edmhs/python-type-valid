
coverage: ## check code coverage quickly with the default Python
	#coverage run --source=tests/ test
	coverage report -m
	coverage html
	$(BROWSER) htmlcov/index.html

test:
	python -m unittest -v
