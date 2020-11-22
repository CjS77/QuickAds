#!/usr/bin/env bash
echo "Setting up database..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput
echo "Copying static files..."
python manage.py collectstatic --noinput
echo "Starting server..."
#python manage.py runserver -v3
gunicorn myproject.wsgi:application --bind 0.0.0.0:8000
