from functools import wraps

from flask import render_template, request, redirect, url_for, abort, session
from minne.models import Token, Score
from core.utils import api

from core.templates import trans


from . import app


def token_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = kwargs.get('token')
        try:
            token_obj = Token.objects.get(key=token, usage_date=None)
            session['language'] = token_obj.client.language
        except Token.DoesNotExist:
            return redirect(url_for('error'))
        return func(*args, **kwargs)
    return wrapper


@app.route('/')
def error():
    return render_template('error.html'), 401


@app.route('/<string:token>/')
@token_required
def home(token):
    response = api('get', '/ping')
    if not response.text == 'pong':
        abort(401, 'The API is currently unavailable. '
              'You should try running this test later.')
    return render_template('intro.html', token=token)


@app.route('/<string:token>/run/')
@token_required
def survey(token):
    try:
        token = Token.objects.get(key=token, usage_date=None)
    except Token.DoesNotExist:
        return render_template('error.html'), 401
    response = api('get', '/questions/tci3240/')
    content = response.json()
    if isinstance(content, dict) and content.get('error'):
        abort(401, content.get('error'))
    questions = [trans(q) for q in content]
    return render_template('survey.html', questions=questions, token=token)


@app.route('/end/', methods=['post'])
def end():
    token = Token.objects.get(key=request.form.get('token'))
    answers = [int(a) for a in request.form.get('answers').split(',')]
    times = [int(t) for t in request.form.get('times').split(',')]
    Score(token=token, answers=answers, times=times,
          client=token.client).save()
    token.void()
    return render_template('end.html')
