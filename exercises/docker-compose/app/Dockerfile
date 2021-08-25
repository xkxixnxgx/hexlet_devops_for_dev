FROM python:3.7.8-slim

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100

WORKDIR /app

RUN apt update && apt install curl -y
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

ENV PATH="${PATH}:/root/.poetry/bin"

COPY pyproject.toml poetry.lock /app/
RUN . $HOME/.poetry/env && poetry update && poetry config virtualenvs.create false && poetry install

ENV PATH="${PATH}:/usr/bin/gunicorn"
RUN whereis gunicorn

EXPOSE 5000 5000

COPY . /app
