import tensorflow as tf
import numpy as np
import sys
from keras.models import Sequential, model_from_json
from keras.layers import Dense, Activation

from sklearn.model_selection import train_test_split

MODEL_NAME = 'model'

def create_keras_model():
    # as first layer in a sequential model:
    model = Sequential()
    model.add(Dense(5, input_shape=(2,)))
    # now the model will take as input arrays of shape (*, 2)
    # and output arrays of shape (*, 1)
    
    # after the first layer, you don't need to specify
    # the size of the input anymore:
    model.add(Dense(1))
    return model

def train_model(model, x_train, y_train):
    model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])
    model.fit(x_train, y_train, epochs=200, batch_size=10, verbose=1)

def save_model(model):
    model_json = model.to_json()
    with open(MODEL_NAME + ".json", "w") as json_file:
        json_file.write(model_json)
    model.save_weights(MODEL_NAME + ".h5")

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
    train_model(model, x_train, y_train)
    save_model(model)
    loaded_model = load_saved_model()
    evaluate(loaded_model, x_test, y_test)

if __name__ == "__main__":
    main()

