#!/bin/bash

./manage.py makemigrations

./manage.py migrate

scrapy crawl tech_crunch

./manage.py runserver
