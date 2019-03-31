import db_service

import flask

from flask import abort, request
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
    if not request.json or not 'title' in request.json:
        abort(400)
    return "<h1>Where you send us your data</h1>"

@app.route('/api/v1/metrics', methods=['GET'])
def fetch_all_metrics():
    return "<h1>You get all the data back</h1>"

INIT_ERROR = db_service.initialize_db()
app.run()
