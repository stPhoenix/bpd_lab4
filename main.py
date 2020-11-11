#-*- coding: utf8 -*-

from flask import Flask, request, render_template
from dh import DH

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = {'error': False, 'message': None, 'data': None, 'action': None}
    if request.method == 'GET':
        return render_template('index.html', name='index', result=result)
    else:
        try:
            result['action'] = request.form['action']
            if request.form['action'] == 'K':
                X = int(request.form['X'])
                Y = int(request.form['Y'])
                Q = int(request.form['Q'])
                result['data'] = DH().calculate_share_secret_key(X, Y, Q)
            elif request.form['action'] == 'keys':
                result['data'] = DH().generate_keys()
        except Exception as e:
            result['action'] = ''
            result['error'] = True
            result['message'] = e
        return render_template('index.html', name='index', result=result)