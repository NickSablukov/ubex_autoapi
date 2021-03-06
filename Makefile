run_dev:
	pip3 install poetry && \
	poetry env use python3.8 && \
	poetry install && \
	poetry run python manage.py migrate && \
	poetry run python manage.py runserver

run_dev_in_docker:
	docker build -t ubex_autoapi . && \
	docker run --rm --network=host ubex_autoapi sh -c "poetry run python manage.py migrate" && \
	docker run -p 8000:8000 --name ubex_autoapi --rm ubex_autoapi

format_code:
	poetry run isort -y
	poetry run black .

check_code:
	poetry run flake8 .
	poetry run isort --check --diff
	poetry run black --check .
	poetry run bandit -r .
	poetry run mypy .

format_and_check_code:
	make format_code
	make check_code
