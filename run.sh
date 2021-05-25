#!/bin/sh

# Opens all ports to be able to access 0.0.0.0
export FLASK_APP=manage.py
export FLASK_ENV=development
flask run --host=0.0.0.0 --port=80

