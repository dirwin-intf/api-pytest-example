dependencies:
	pip3 freeze > requirements

install:
	pip3 install -r requirements.txt
