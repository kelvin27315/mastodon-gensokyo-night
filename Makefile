test:
	poetry run python -m unittest

lint:
	docker compose run pysen lint

format:
	docker compose run pysen format
