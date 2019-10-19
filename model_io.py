import os
from keras.models import model_from_json
MODEL_NAME = 'model'

def save_model(model):
    model_json = model.to_json()
    with open(MODEL_NAME + ".json", "w") as json_file:
        json_file.write(model_json)
    model.save_weights(MODEL_NAME + ".h5")

def load_saved_model():
    # load json and create model
    directory = os.path.dirname(os.path.realpath(__file__))
    json_file = open(os.path.join(directory, MODEL_NAME + '.json'), 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights(MODEL_NAME + ".h5")
    print("Loaded model from disk")
    return loaded_model
 
