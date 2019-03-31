import db_service

import json
import jsonschema

schema = {
    "type": "object",
    "metric": {
        "type": "object",
        "required": ["name", "value", "date"]},
    "required": ["metric"]
}

def initialize_db():
    return db_service.initialize_db()

def add_data_to_db(data_json):
    """ iterate over received metrics and add them to the db """
    try:
        jsonschema.validate(data_json, schema)
    except jsonschema.exceptions.ValidationError as e:
        return e, 400
    pass

def _process_json_data(data_json):
    """ process json request if necessary """
    pass

def fetch_stats():
    """ process data to get stats and create a json with them """
    pass

def fetch_stored_data ():
    """ get data from the db and return it in a json """
    pass

def _convert_db_data_to_json():
    """ transform db response to json object """
    pass