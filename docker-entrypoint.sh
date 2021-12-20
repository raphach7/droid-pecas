#!/bin/bash -x

sleep 10 &&
python manage.py migrate --noinput &&
python manage.py runserver 0.0.0.0:8000 || exit 1
exec "$@"