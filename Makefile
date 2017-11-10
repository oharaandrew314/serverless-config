init:
	pipenv install --dev

clean:
	rm -rf dist build
	pipenv run setup.py clean --all

test:
	pipenv run pytest tests --cov-report term-missing --cov --blockage
	pipenv run flake8

package: clean
	python setup.py bdist_wheel --universal

publish-test: package
	pip install -q twine
	twine upload -r pypitest dist/*

publish: package
	pip install -q twine
	twine upload -r pypi dist/*

dev-mode:
	pip install -e . --upgrade