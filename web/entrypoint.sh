#!/bin/sh

python manage.py create_db
python manage.py seed_db

exec "$@"
