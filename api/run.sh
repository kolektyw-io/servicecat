#!/bin/bash

python -m manage migrate
python -m manage collectstatic --noinput
gunicorn -w 32 --threads 4 -t 120 -b 0.0.0.0:8000 api.wsgi