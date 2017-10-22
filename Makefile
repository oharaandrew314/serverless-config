init:
	pipenv install --dev

clean:
	rm -rf dist build
	pipenv run setup.py clean --all

test:
	pipenv run pytest tests --flake8 --cov-report term-missing --cov --blockage

package:: clean
	pipenv run setup.py bdist_wheel --universal

publish-test: package
	twine upload -r pypitest dist/*

publish: package
	twine upload -r pypi dist/*

dev-mode:
	pip install -e . --upgrade