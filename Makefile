environment:
	python3 -m venv env

dependencies:
	pip3 freeze > requirements.txt

install:
	pip3 install -r requirements.txt
