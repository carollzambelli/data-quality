export PYTHONPATH = ./quality
export CONFIG_PATH = ./assets/configs.json

venv:
	python -m venv venv 
	venv\Scripts\activate && pip install -r requirements.txt 

venv_run_test:
	venv\Scripts\activate && pip install pytest
	venv\Scripts\activate && pytest tests/quality_test.py

venv_remove:
	rmdir /S /Q venv

all: venv venv_run_test venv_remove