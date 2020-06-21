FROM python:3.8-alpine as base

RUN apk add --no-cache alpine-sdk git postgresql-dev openssl-dev libxml2-dev \
    libxslt-dev openssh-client libffi-dev

RUN pip3 install pip --upgrade
RUN pip3 install poetry==1.0.0

WORKDIR /app
RUN poetry config virtualenvs.create false
ADD pyproject.toml /app/
ADD poetry.lock /app/

RUN poetry install --no-dev --no-interaction --no-ansi -vvv

ADD . /app
EXPOSE 8000
CMD ["poetry", "run", "gunicorn", "-c", "gunicorn.conf.py", "-b", "0.0.0.0:8000", "project.wsgi"]
