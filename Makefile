init:
	pip install --quiet -r requirements.txt

clean:
	rm -rf dist build
	python setup.py clean --all

test:
	pytest tests --flake8 --cov-report term-missing --cov --blockage

package:: clean
	python setup.py bdist_wheel --universal

publish-test: package
	twine upload -r pypitest dist/*

publish: package
	twine upload -r pypi dist/*

dev-mode:
	pip install -e .