#!/usr/bin/env bash
# exit on error
set -o errexit

python -m pip install pipenv

pipenv install

pipenv run python manage.py collectstatic --no-input
pipenv run python manage.py migrate

# Check if a superuser already exists
SUPERUSER_EXISTS=$(pipenv run python manage.py shell -c "from django.contrib.auth.models import User; print(User.objects.filter(is_superuser=True).exists())")

# Create superuser only if it doesn't exist
if [ "$SUPERUSER_EXISTS" = "False" ]; then
    pipenv run python manage.py createsuperuser --noinput
fi
