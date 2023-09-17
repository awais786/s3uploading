runserver:
	python manage.py runserver 127.0.0.1:8080

makemigrations: ## Apply database migrations
	python manage.py makemigrations --noinput

migrate: ## Apply database migrations
	python manage.py migrate --noinput

requirements:
	@echo "#######################################################################"
	@echo "#################### Installing dev environment #######################"
	@echo "#################### (it may take some time...) #######################"
	@echo "#######################################################################"
	@pip install -r requirements.txt

runserver:
	python manage.py runserver

install_requirements:
	pip install -r requirements.txt
	python manage.py migrate
	python manage.py shell < add_superuser.py


