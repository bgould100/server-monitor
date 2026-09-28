import json
import os
from config_test import load_config, validate_server
from pathlib import Path
filename = os.environ.get("SERVER_FILE")


result = load_config(filename)
if result is not None:
    for item in result:
        if validate_server(item):
            print(f"{item['name']}: Valid")
        else:
            print(f"{item['name']}: Invalid")


