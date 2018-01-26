from flask import session
from csvi18n import Translator

from . import app


def trans(sentence):
    language = session.get('language')
    if not language:
        return sentence
    filename = app.config['TRANSLATION_FILES'].get(language)
    translator = Translator(filename,
                            cache=app.config.get('TRANSLATION_CACHE'))
    return translator.translate(sentence)


@app.context_processor
def context_processor():
    return {
        'trans': trans,
        '_': trans,
        'language': session.get('language'),
    }
