install: .env
	@poetry install

.env:
	@test ! -f .env && cp .env.example .env

create_migration:
	@poetry run flask db init

generate_init_migration: create_migration
	@poetry run flask db migrate -m "Initial migration."

migration: generate_init_migration
	@poetry run flask db upgrade	

run:
	@poetry run gunicorn -w 4 --bind 0.0.0.0:5000 wsgi:app

generate_secret:
	@python -c 'import secrets; print(secrets.token_hex())'

lint:
	@poetry run flake8 app

test:
	@poetry run pytest app

test-coverage:
	@poetry run pytest --cov=app

requirements.txt: poetry.lock
	@poetry export -f requirements.txt --output requirements.txt --without-hashes

.PHONY: install requirements.txt