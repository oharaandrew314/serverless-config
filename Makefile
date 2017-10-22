init:
	pip install --quiet -r requirements.txt

clean:
	python setup.py clean --all

test:
	pytest tests --blockage

test-full:
	pytest tests --flake8 --cov-report term-missing --cov --blockage

coverage:
	pytest tests --cov-report term-missing --cov --blockage

lint:
	flake8 serverless_config