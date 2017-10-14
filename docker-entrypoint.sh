#!/bin/bash
python3.6 manage.py migrate        # Apply database migrations
python3.6 manage.py collectstatic --clear --noinput # clearstatic files
python3.6 manage.py collectstatic --noinput  # collect static files
# Prepare log files and start outputting logs to stdout
touch /srv/logs/gunicorn.log
touch /srv/logs/access.log
tail -n 0 -f /srv/logs/*.log &
echo Starting nginx 
# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn simplesocial.wsgi:application --name simplesocial --bind unix:simplesocial.sock --workers 3 --log-level=info --log-file=/srv/logs/gunicorn.log --access-logfile=/srv/logs/access.log & 
exec nginx

