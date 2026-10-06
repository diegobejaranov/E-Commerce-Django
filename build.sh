#!/usr/bin/env bash
# Salir inmediatamente si ocurre un error
set -o errexit

# Instalar las librerías del proyecto
pip install -r requirements.txt

# Recopilar los archivos estáticos de Bootstrap en una sola carpeta
python manage.py collectstatic --noinput

# Aplicar las tablas de la base de datos
python manage.py migrate
