#!/bin/sh

# if any error occurs, let script fail
set -e

python manage.py wait_for_db
# let all static files be copied to the static directory defined in settings.py
python manage.py collectstatic --noinput
python manage.py migrate

# run uwsgi service on tcp socket 9000 (ngnix-server) using 4 workers
# module points to djangovuecrudapi/wsgi.py
uwsgi --socket :9000 --workers 4 --master --enable-threads --module DjangoVueCrudAPI.wsgi
