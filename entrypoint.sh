#!/bin/sh
python3 manage.py collectstatic --noinput
gunicorn --config gunicorn_config.py

