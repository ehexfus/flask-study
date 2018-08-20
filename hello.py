# coding=utf-8
from flask import Flask

'''create app'''
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


app.run(host='127.0.0.1', port=8080, debug=True)
