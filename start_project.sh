#! /bin/bash
python manage.py collectstatic --no-input
python manage.py migrate --no-input
exec gunicorn -c /bin/gunicorn_config.py conf.wsgi