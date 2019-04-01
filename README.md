# execution
Install requirements.txt
`pip install -r requirements.txt`

Start API
`python3 api/api_controller.py`

Start client
`python3 client/client.py --import FOLDER_PATH`

### json format
The json structure to upload data should look like this:
`
{'id':{
  'name':'#name',
  'value':'#value',
  'timestamp':'#timestamp'
  }
}  
`

## What is working
API health

API import data

API get all data

## What is missing
API get stats

Avoid duplicated entries

Parallel file upload

THE TESTS!

## What is broken
file reader in the client does not generate the right json format
