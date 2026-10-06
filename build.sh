#!/usr/bin/env bash
# Salir inmediatamente si ocurre un error
set -o errexit

# Instalar las librerías del proyecto
pip install -r requirements.txt

# Recopilar los archivos estáticos de Bootstrap en una sola carpeta
python manage.py collectstatic --noinput

# Aplicar las tablas de la base de datos
python manage.py migrate

export DJANGO_SETTINGS_MODULE=TiendaOnline.settings

python -c "import django; django.setup(); from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@ejemplo.com', 'Colombia1234')"
