import numpy as np
from parse_input import parse_input

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
    model_dict = dict()
    model_dict["plus"] = load_saved_model("plus")
    model_dict["minus"] = load_saved_model("minus")
    model_dict["multiply"] = load_saved_model("multiply")
    model_dict["divide"] = load_saved_model("divide")
    while True:
        print("Input first value:")
        a = input()
        print("Input second value:")
        b = input()
        print("Input operator:")
        method = parse_input(input())

        print(get_answer(model_dict[method], a, b))

