import os
import pickle


class Inference(object):
    model = None

    def __init__(self, model_path, model_name):
        self.model_path = model_path
        self.model_name = model_name

    def get_model(self):
        """Get the model object for this instance, loading it if it's not already loaded."""
        if self.model is None:
            with open(os.path.join(self.model_path, self.model_name), 'rb') as inp:
                self.model = pickle.load(inp)
        return self.model

    def predict(self, input_str):
        return self.predict(input_str)
