import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/api/v1/health', methods=['GET'])
def healtch_check():
    return "<h1>This will eventually tell you if system is running</h1>"

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
