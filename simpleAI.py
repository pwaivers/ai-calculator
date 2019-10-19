import tensorflow as tf
import numpy as np
import sys
from keras.models import Sequential, model_from_json
from keras.layers import Dense, Activation

from sklearn.model_selection import train_test_split

MODEL_NAME = 'model'

def load_saved_model():
    # load json and create model
    json_file = open(MODEL_NAME + '.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights(MODEL_NAME + ".h5")
    print("Loaded model from disk")
    return loaded_model

def get_answer(model, a, b):
    a = float(a)
    b = float(b)
    inp = np.array([[a, b]], dtype = np.float64)
    return model.predict(inp)

if __name__ == "__main__":
    model = load_saved_model()
    while True:
        print("Input first value:")
        a = input()
        print("Input second value:")
        b = input()
        print(get_answer(model, a, b))

