from flask import Flask
from flask import request
from model_io import load_saved_model
from simple_ai import get_answer
import random

app = Flask(__name__)

@app.route('/')
def hello():
    return "I am alive!"
    
@app.route('/test')
def test():
    global testvar
    return "Var is: " + str(testvar)
    
@app.route('/ai-add')
def ai_add():
    model = load_saved_model()
    left = request.args.get('left')
    right = request.args.get('right')
    return str(get_answer(model, left, right))

