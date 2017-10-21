init:
	pip3 install -r requirements.txt

test:
	pytest tests --flake8 --cov-report term-missing --cov --blockage