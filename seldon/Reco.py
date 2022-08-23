class Reco(object):

    def __init__(self):
        print("Initializing")

    def predict(self, X, features_names):
        print("Predict called - will run identity function")
        return X
