install:
	#install commands
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:
	#format
	black *.py mylib/*.py
lint:
	#pylint
	pylint --disable=R, *.py mylib/*.py
test:
	#test
deploy:
	#deploy
all: install format lint test deploy
