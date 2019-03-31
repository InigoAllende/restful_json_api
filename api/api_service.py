import db_service

import json
import jsonschema

schema = {
    "type": "object",
    "id": {
        "type": "object",
        "required": ["name", "value", "date"]}
}

def initialize_db():
    return db_service.initialize_db()

def add_data_to_db(data_json):
    """ iterate over received metrics and add them to the db """
    try:
        jsonschema.validate(data_json, schema)
        db_service.insert_metrics(data_json)
    except jsonschema.exceptions.ValidationError as e:
        return e, 400
    except Exception as e:
        return e, 500
    return None, 200

def _process_json_data(data_json):
    """ process json request if necessary """
    pass

def fetch_stats():
    """ process data to get stats and create a json with them """
    pass

def fetch_stored_data ():
    """ get data from the db and return it in a json """
    return _convert_db_data_to_json(db_service.get_all_data())
    
def _convert_db_data_to_json(db_data):
    """ transform db response to json object """
    json_data = {}
    for index in range(len(db_data)):
        name, value, timestamp = db_data[index]
        json_data[index] = {'name': name, 'value': value, 'timestamp': timestamp}
    return json.dumps(json_data)