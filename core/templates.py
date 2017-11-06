from flask import g, request
from tcii18n.template import flask_methods

from . import app


def get_translations_file():
    language = 'en'
    return app.config.get('TRANSLATION_FILES').get(language)


flask_methods(app, get_translations_file)
