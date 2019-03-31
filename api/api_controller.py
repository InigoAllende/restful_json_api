import api_service

import flask

from flask import abort, jsonify, request
from flask_api import status

app = flask.Flask(__name__)
app.config["DEBUG"] = True

INIT_ERROR = None

@app.route('/api/v1/health', methods=['GET'])
def healtch_check():
    """ Check if db is up and running """
    if (INIT_ERROR):
        abort(503)
    return 'everything is ok', status.HTTP_200_OK

@app.route('/api/v1/metrics/stats', methods=['GET'])
def fetch_stats():
    return "<h1>Here you will see overall stats</h1>"

@app.route('/api/v1/metrics', methods=['POST'])
def load_metrics():
    if not request.json:
        abort(400)
    # TODO: think of a better way to retrieve error/success
    exception, code = api_service.add_data_to_db(request.json)
    if exception:
        return str(exception), code
    return 'data added', status.HTTP_200_OK

@app.route('/api/v1/metrics', methods=['GET'])
def fetch_all_metrics():
    try:
        return jsonify(api_service.fetch_stored_data()), status.HTTP_200_OK
    except Exception:
        abort(500)

INIT_ERROR = api_service.initialize_db()
app.run()
