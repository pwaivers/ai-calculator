import tensorflow as tf
import numpy as np
import sys
from model_io import create_keras_model, save_model, load_saved_model

from sklearn.model_selection import train_test_split

def train_model(model, x_train, y_train, n_epochs=200):
    model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])
    model.fit(x_train, y_train, epochs=n_epochs, batch_size=10, verbose=1)
   
def evaluate(loaded_model, x_test, y_test):
    # evaluate loaded model on test data
    loaded_model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])
    score = loaded_model.evaluate(x_test, y_test, verbose=0)
    print("%s: %.2f%%" % (loaded_model.metrics_names[1], score[1]*100))
    return score

# Creates size-n^2 training data set of a + b for a,b from 0 to n-1
def load_training_data(n):
    a, b = np.meshgrid(np.arange(n), np.arange(n))
    x_data = np.vstack([a.flatten(), b.flatten()]).T
    y_data = np.sum(x_data, axis=1)
    print("X_data")
    print(x_data)
    print("Y data")
    print(y_data)
    return train_test_split(x_data, y_data)

def main():
    x_train, x_test, y_train, y_test = load_training_data(10)
    print("Training data:")
    print(x_train.shape)
    print(y_train.shape)
    model = create_keras_model()
    train_model(model, x_train, y_train, 200)
    save_model(model)
    loaded_model = load_saved_model()
    evaluate(loaded_model, x_test, y_test)

if __name__ == "__main__":
    main()

