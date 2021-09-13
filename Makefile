PIP:=venv/bin/pip
PYTHON:=venv/bin/python3
DJANGO-ADMIN:=venv/bin/django-admin
SETTINGSFILE:=--settings=src.settings.local

define create-env
python3 -m pip install virtualenv
python3 -m virtualenv venv
endef

venv:
	@$(create-env)
	venv/bin/python -m pip install -r requirements.txt

install:
	venv/bin/python -m pip install -r requirements.txt

migrate:
	@$(PYTHON) manage.py makemigrations $(SETTINGSFILE)
	@$(PYTHON) manage.py migrate $(SETTINGSFILE)

createuser:
	@$(PYTHON) manage.py createsuperuser $(SETTINGSFILE)

run:
	@$(PYTHON) manage.py runserver $(SETTINGSFILE)

shell:
	@$(PYTHON) manage.py shell $(SETTINGSFILE)


help:
	@echo "make venv       -> para criar a maquina virtual"
	@echo "make migrate    -> para atualizar o banco"
	@echo "make createuser -> para criar um novo usuario root"
	@echo ""