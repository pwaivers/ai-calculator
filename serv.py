from flask import Flask
from flask import request
from model_io import create_keras_model, get_weights_file
from simple_ai import get_answer
import random

app = Flask(__name__)

model = ''

@app.route('/')
def hello():
    global model
    model = create_keras_model()
    model.load_weights(get_weights_file())
    model._make_predict_function()
    return "I am alive!"
    
@app.route('/test')
def test():
    global testvar
    return "Var is: " + str(testvar)
    
@app.route('/ai-add')
def ai_add():
    global model
    if model == '':
        return "No model"

    left = request.args.get('left')
    right = request.args.get('right')
    return str(get_answer(model, left, right))

