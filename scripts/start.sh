#!/usr/bin/env bash
python manage makemigrations
python manage.py migrate
python manage.py collectstatic
