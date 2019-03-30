import flask
import sqlite3

from flask_api import status
from sqlite3 import Error

app = flask.Flask(__name__)
app.config["DEBUG"] = True

DB_CONN = None

@app.route('/api/v1/health', methods=['GET'])
def healtch_check():
    """ Check if db is up and running """
    if (not _create_connection()):
        return 'everything is ok', status.HTTP_200_OK
    return 'ups, there seems to be an error on our side', status.HTTP_503_SERVICE_UNAVAILABLE

def _create_connection():
    """ create a database connection to a SQLite database """
    try:
        DB_CONN = sqlite3.connect('metrics.db')
    except Error as e:
        return e

@app.route('/api/v1/metrics/stats', methods=['GET'])
def fetch_stats():
    return "<h1>Here you will see overall stats</h1>"

@app.route('/api/v1/metrics', methods=['POST'])
def load_metrics():
    return "<h1>Where you send us your data</h1>"

@app.route('/api/v1/metrics', methods=['GET'])
def fetch_all_metrics():
    return "<h1>You get all the data back</h1>"

app.run()
