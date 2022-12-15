import json
import os
import flask

from inference import Inference

default_model_path_prefix = '/opt/ml/'

app = flask.Flask(__name__)

model_path = os.getenv('MODEL_PATH', default=default_model_path_prefix)
model_name = os.getenv('MODEL_NAME', default='model.pkl')

inference = Inference(model_path=model_path, model_name=model_name)


@app.route('/ping', methods=['GET'])
def ping():
    health = inference.get_model() is not None
    status = 200 if health else 404
    return flask.Response(response='\n', status=status, mimetype='application/json')


@app.route('/invocations', methods=['POST'])
def transformation():
    if flask.request.content_type == 'application/json':
        in_data = flask.request.get_json()
        s = in_data['input_str']
        print('calling with {}'.format(s))
    else:
        return flask.Response(response='This predictor only supports application/json data', status=415,
                              mimetype='text/plain')

    print('Invoked with {}'.format(s))
    predictions = inference.predict(s)
    return flask.Response(response=json.dumps(predictions), status=200, mimetype='text/csv')
