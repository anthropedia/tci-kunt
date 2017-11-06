import os
import sys

from flask import Flask
from tciminne import db

settings_file = 'settings'
if 'unittest' in sys.argv[0]:
    settings_file = 'settings.test'

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__) + '/..')
os.environ.setdefault('SETTINGS', f'{PROJECT_PATH}/{settings_file}.py')

app = Flask('tki-kund')
app.config.from_envvar('SETTINGS')

app.root_path = PROJECT_PATH
app.secret_key = app.config['SECRET_KEY']

db.connect(**app.config['DATABASE'])

from core import views, templates  # noqa: F401
