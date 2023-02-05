#!/bin/bash

# Collect static files
echo "Collect static files"
python3 manage.py collectstatic --noinput
exec "$@"

# Make migrations
echo "Make migrations"
python3 manage.py makemigrations --noinput

# Apply database migrations
echo "Apply database migrations"
python3 manage.py migrate --noinput


