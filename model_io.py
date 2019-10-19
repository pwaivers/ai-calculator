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
    return model


def save_model(model):
    model_json = model.to_json()
    with open(MODEL_NAME + ".json", "w") as json_file:
        json_file.write(model_json)
    model.save_weights(MODEL_NAME + ".h5")

def get_directory():
    return os.path.dirname(os.path.realpath(__file__))

def get_weights_file():
    # load weights into new model
    return os.path.join(get_directory(), MODEL_NAME + ".h5")

def load_saved_model():
    # load json and create model
    directory = get_directory()
    json_file = open(os.path.join(directory, MODEL_NAME + '.json'), 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights(get_weights_file())
    print("Loaded model from disk")
    return loaded_model
 

