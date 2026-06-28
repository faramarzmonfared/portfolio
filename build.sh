#!/usr/bin/env bash
set -o errexit

poetry install --only main
poetry run python manage.py collectstatic --noinput
poetry run python manage.py migrate