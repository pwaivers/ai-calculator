import os
from keras.models import model_from_json
from keras.models import Sequential
from keras.layers import Dense, Activation
MODEL_NAME = 'model'

def create_keras_model():
    # as first layer in a sequential model:
    model = Sequential()
    model.add(Dense(5, input_shape=(2,)))
    # now the model will take as input arrays of shape (*, 2)
    # and output arrays of shape (*, 1)
    
    # after the first layer, you don't need to specify
    # the size of the input anymore:
    model.add(Dense(5))
    model.add(Dense(1))
    model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])
    return model

def get_directory():
    return os.path.dirname(os.path.realpath(__file__))

def get_weights_file(method):
    return os.path.join(get_directory(), MODEL_NAME + "_" + method + ".h5")

def get_json_file(method):
    return os.path.join(get_directory(), MODEL_NAME + "_" + method + '.json') 

def save_model(model, method):
    model_json = model.to_json()
    with open(get_json_file(method), "w") as json_file:
        json_file.write(model_json)
    model.save_weights(get_weights_file(method))

def load_saved_model(method):
    # load json and create model
    json_file = open(get_json_file(method), 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights(get_weights_file(method))
    print("Loaded model from disk")
    return loaded_model
 

