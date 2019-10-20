from flask import Flask, send_from_directory, request
from parse_input import parse_input
import model_io as m_io
from simple_ai import get_answer
import random

import psycopg2
import os

import numpy

DB_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DB_URL, sslmode='require')


app = Flask(__name__, static_url_path='')

model = ''
models = {}

@app.route('/')
def root():
    return app.send_static_file('index.html')
    
@app.route('/test')
def test():
    global testvar
    return "Var is: " + str(testvar)
    
@app.route('/ai-add')
def ai_add():
    global model
    if model == '':
        model = m_io.create_keras_model()
    method = parse_input(request.args.get('operator'))
    model.load_weights(m_io.get_weights_file(method))
    model._make_predict_function()

    left = request.args.get('left')
    right = request.args.get('right')
    return str(get_answer(model, left, right))

@app.route('/save-models')
def save_models():
    global models
    global conn
    cur = conn.cursor()
    
    for m in models:
        cur = conn.cursor()#putting this here because I am worried about the insert statment possibly mucking up the check to see if the record exists
        #save model -> get file paths -> read files and save into db
        save_model(models[m], m)
        wghts = b''
        with open(m_io.get_weights_file(m), "rb") as f:
            wghts = f.read()
        json = b''
        with open(m_io.get_json_file(m), "rb") as f:
            json = f.read()
        cur.execute('SELECT * FROM models WHERE name = %s', (m,))
        r = cur.fetchone()
        
        if r is not None:
            cur.execute('UPDATE models SET weights = %s, json = %s WHERE name = %s', (wghts, json, m,))
        else:
            cur.execute('INSERT INTO models(name, weights, json) VALUES (%s, %s, %s)', (m, wghts, json,))
        
        cur.commit()
            
