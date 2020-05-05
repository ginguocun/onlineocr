#!/bin/sh

/etc/init.d/nginx start
uwsgi --ini /opt/onlineocr/uwsgi.ini