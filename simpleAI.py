import numpy as np
from model_io import load_saved_model


MODEL_NAME = 'model'

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

