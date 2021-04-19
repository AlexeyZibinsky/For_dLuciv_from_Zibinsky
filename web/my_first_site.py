#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# A very simple Flask Hello World app for you to get started with...

import flask
from flask import Flask, request

def algoritm_Evklida(a, b):
    a, b = abs(a), abs(b)
    while True:
        if a > b:
            a -= b
        elif b > a:
            b -= a
        else:
            return a

app = Flask(__name__, static_folder="static", static_url_path="", template_folder="templates")

@app.route('/hello/<string:text>')
@app.route('/hello')
def hello_world(text=None):
    return 'Just a plain text: "Hello from Flask!"' + (' With param ' + text if text else '')


@app.route('/')
def root():
    return flask.render_template(
        'index.html'
    )


@app.route('/name', methods = ['GET', 'POST'])
def hello_name(alg = algoritm_Evklida):
    result = ''

    if request.method == 'GET':
        name_param=request.args.get('name')
    elif request.method == 'POST':
        name_param=request.form.get('name')

    if name_param==None:
        name_param="вводить тут"

    if name_param != "вводить тут":
        tmp = (list(map(int, name_param.split(','))))
        result = alg(tmp[0], tmp[1])
        print(result)

    return flask.render_template(
        'name.html',
        name=result,
        method=request.method
    )


if __name__ == '__main__':
   app.run(debug = True)