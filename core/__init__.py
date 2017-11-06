import os

from flask import Flask
from tcidatabase import db

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__) + '/..')
os.environ.setdefault('SETTINGS', PROJECT_PATH + '/settings.py')

app = Flask('tki-kund')
app.config.from_envvar('SETTINGS')

app.root_path = PROJECT_PATH
app.secret_key = app.config['SECRET_KEY']

db.connect(**app.config['DATABASE'])
