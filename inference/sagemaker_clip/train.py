import dill as pickle


class Model:
    def predict(x: str):
        sentence = "Hello World! " + x
        return sentence


with open('model.pkl', 'wb') as f:
    pickle.dump(Model, f)

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

out = model.predict("stuff")
print(out)