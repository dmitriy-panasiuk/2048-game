test:
	tox -e unit

run:
	export PYTHONPATH=./src/
	python ./src/main.py