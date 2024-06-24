#!/bin/sh
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py loaddata mock-data/area_subarea_pesquisador_agencia.json
python3 manage.py loaddata mock-data/projeto_valores_producoes.json

ADMIN_PWD=$PASSWORD

python3 manage.py createsuperuser --noinput --username admin --email admin@admin.com
echo "from django.contrib.auth.models import User; user = User.objects.get(username='admin'); user.set_password('$ADMIN_PWD'); user.save()" | python3 manage.py shell


python3 manage.py collectstatic --noinput
gunicorn --config gunicorn_config.py

