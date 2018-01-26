from pathlib import Path
import sys

from flask import Flask
from minne import db


settings_file = 'settings.py'
if 'unittest' in sys.argv[0]:
    settings_file = 'settings.test.py'

PROJECT_PATH = Path(__file__).parent.parent

app = Flask('tki-kund')
app.config.from_pyfile(PROJECT_PATH / 'settings.default.py')
app.config.from_pyfile(PROJECT_PATH / settings_file, silent=True)

app.root_path = PROJECT_PATH
app.secret_key = app.config['SECRET_KEY']

db.connect(**app.config['DATABASE'])

from core import views, templates  # noqa: F401
