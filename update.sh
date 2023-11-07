#!/bin/bash

git pull
python /root/FIXMASTER/manage.py collectstatic --noinput
python /root/FIXMASTER/manage.py migrate
python /root/FIXMASTER/manage.py runserver 0.0.0.0:8000&
