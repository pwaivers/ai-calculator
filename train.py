import tensorflow as tf
import numpy as np
import sys
from model_io import create_keras_model, save_model, load_saved_model
from load_training_data import load_training_data


def train_model(model, x_train, y_train, n_epochs=200):
    model.fit(x_train, y_train, epochs=n_epochs, batch_size=10, verbose=1)
   
def evaluate(loaded_model, x_test, y_test):
    # evaluate loaded model on test data
    loaded_model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])
    score = loaded_model.evaluate(x_test, y_test, verbose=0)
    print("%s: %.2f%%" % (loaded_model.metrics_names[1], score[1]*100))
    return score

def create_and_train_model(method="plus", n_epochs=200):
    x_train, x_test, y_train, y_test = load_training_data(10, method)
    print("Training data:")
    print(x_train.shape)
    print(y_train.shape)
    model = create_keras_model()
    train_model(model, x_train, y_train, n_epochs)
    save_model(model, method)
    loaded_model = load_saved_model(method)
    evaluate(loaded_model, x_test, y_test)

if __name__ == "__main__":
    create_and_train_model("plus")
    create_and_train_model("minus")
    create_and_train_model("multiply", 500)
    create_and_train_model("divide", 500)

