import numpy as np

def get_answer(model, a, b):
    a = float(a)
    b = float(b)
    print("First value:")
    print(a)
    print("Seconds value:")
    print(b)
    inp = np.array([[a, b]], dtype = np.float64)
    output_raw = model.predict(inp)
    return output_raw[0][0]

if __name__ == "__main__":
    from model_io import load_saved_model
    model = load_saved_model()
    while True:
        print("Input first value:")
        a = input()
        print("Input second value:")
        b = input()
        print(get_answer(model, a, b))

