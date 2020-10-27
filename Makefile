.PHONY: build run

build:
	pip install -r requirements.txt
	#pyuic5 -x ui.ui -o ui.py

run:
	python main.py