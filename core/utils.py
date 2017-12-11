import requests
from flask import jsonify

from core import app


def api(method, endpoint, data=None, *args, **kwargs):
    url = '{}{}'.format(app.config['TCIAPI_URL'], endpoint)
    if 'headers' not in kwargs:
        kwargs['headers'] = {}
    kwargs['headers'].setdefault('Content-Type', 'application/json')
    kwargs['headers'].setdefault('Authentication', 'Bearer {}'.format(
        app.config['TCIAPI_TOKEN']
    ))
    if data:
        kwargs['data'] = jsonify(data).data
    return getattr(requests, method)(url, *args, **kwargs)
