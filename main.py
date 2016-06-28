# -*- coding: utf-8 -*-
"""`main` is the top level module for your Flask application."""

# from google.appengine.ext import ndb
# from flask import jsonify 

# Import the Flask Framework
from flask import Flask 

from util import store_manager

app = Flask(__name__)
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server. 

# 초기화
storeList = store_manager.get_store_list()

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!22'

@app.route('/other')
def helloOther():
    """Return a friendly HTTP greeting."""
    return ''.join(storeList) + 'added'


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500



