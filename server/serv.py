from flask import Flask
from flask import request
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
    left = int(request.args.get('left'))
    right = int(request.args.get('right'))
    return str(left + right + random.randint(1, 13))

