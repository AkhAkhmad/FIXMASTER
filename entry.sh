#!/bin/bash
python3 manage.py makemigrations && python3 manage.py migrate && celery -A FIXMASTER worker -l INFO && celery -A FIXMASTER beat -l INFO && python3 manage.py runserver 0.0.0.0:8000
