from flask import render_template, request
from tciminne.models import Token, Score
from tcidata import get_tci

from . import app


@app.route('/')
def home():
    return render_template('error.html'), 401


@app.route('/<string:token>')
def survey(token):
    try:
        token = Token.objects.get(key=token, usage_date=None)
    except Token.DoesNotExist:
        return render_template('error.html'), 401
    tci = get_tci('tci-3-240')
    questions = tci.get('questions')
    return render_template('survey.html', questions=questions, token=token)


@app.route('/end', methods=['post'])
def end():
    token = Token.objects.get(key=request.form.get('token'))
    answers = [int(a) for a in request.form.get('answers').split(',')]
    times = [int(t) for t in request.form.get('times').split(',')]
    Score(token=token, answers=answers, times=times).save()
    token.void()
    return render_template('end.html')
