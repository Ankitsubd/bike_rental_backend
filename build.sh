#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input

# Only run migrations if database doesn't exist
if [ ! -f "db.sqlite3" ]; then
    python manage.py migrate
    echo "Database initialized"
else
    echo "Database already exists, skipping migration"
fi 