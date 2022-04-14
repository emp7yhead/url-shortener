init_db:
	@poetry run python3 -m init_db

run:
	@poetry run flask run

generate_secret:
	@python -c 'import secrets; print(secrets.token_hex())'

