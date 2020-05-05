#!/bin/sh

/etc/init.d/nginx start
python3 /opt/onlineocr/manage.py migrate
uwsgi --ini /opt/onlineocr/uwsgi.ini