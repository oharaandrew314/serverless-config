init:
	pip install --quiet -r requirements.txt

clean:
	rm -rf dist build
	python setup.py clean --all

test:
	pytest tests --flake8 --cov-report term-missing --cov --blockage

publish-test: clean
	python setup.py bdist_wheel --universal
	twine upload -r pypitest dist/*

publish: clean
	python setup.py bdist_wheel --universal
	twine upload -r pypi dist/*

dev-mode:
	pip install -e .