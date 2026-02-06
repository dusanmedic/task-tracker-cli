import json

FILE_NAME = 'data.json'

def load_data():
    try:
        with open(FILE_NAME, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"tasks":[]}    

def save_data(data):
    with open(FILE_NAME, 'w') as f:
        json.dump(data, f, indent=4)
