import csv
import json
import requests
import sys
import os
import pandas as pd

# parser = argparse.ArgumentParser(description='Upload data to service.')
# parser.add_argument('files', metavar='PATH', type=str, nargs='+',
#                     help='A file or folder with files to upload')
# parser.add_argument('--import',
#                     help='Specifies what the client should do with the data')
# args = parser.parse_args()

def upload_data():
    _validate_args()
    files = _get_files(sys.argv[2])
    _send_data(sys.argv[2], files)

def _send_data(path, file_list):
    """ iterate over the files and upload the data """
    for item in file_list:
        if str(item).endswith('.csv'):
            data = _read_contents(os.path.join(path, item))
            _send_request(data)

def _read_contents(file):
    """ open file and return its contents as json """
    with open(file) as csvdata:
        next(csvdata, None) # skip the headers
        reader = csv.DictReader(csvdata,fieldnames=['name', 'value','timestamp'])
        print(json.dumps([row for row in reader]))
        return json.dumps([row for row in reader])

def _send_request(data):
    """ send a request with the file data json in the body """
    r = requests.post('http://127.0.0.1:5000/api/v1/metrics', json=data)
    print('***********')
    print(r)

def _get_files(path):
    try:
        print(path)
        return os.listdir(path)
    except:
        print('provided path is not valid')
        sys.exit(2)

def _validate_args():
    """ Assert arguments are valid
        TODO: do it in a nice way
    """
    if len(sys.argv) < 3:
        print('Number of arguments provided is not correct')
        print('client.py --import <path of files to upload>')
        sys.exit(2) 
    elif sys.argv[1] != '--import':
        print('invalid argument %s' % sys.argv[1])
        sys.exit(2)

upload_data()