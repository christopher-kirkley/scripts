#!/usr/bin/env python3

import pathlib
import os

template_path = '/Users/ck/Documents/programming/templates/flask_app.py'
current_path = pathlib.Path().absolute()

flask_app = input("Enter flask app: ")
flask_app = flask_app + '.py'

with open(template_path) as file:
    with open(flask_app, 'w') as new_file:
        for line in file.readlines():
            new_file.write(line)

