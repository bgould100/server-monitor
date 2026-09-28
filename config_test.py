import os
import json
from pathlib import Path

def load_config(filename):
    if filename is not None:
        file_path = Path(filename)
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                print(f"Configuration file found: {file_path}")
                if type(data) == list:
                    return data
                else:
                    print("JSON not a list.")
        except json.JSONDecodeError:
            print("JSON data damaged.")
        except FileNotFoundError:
            print("Configuration file not found.")
        except PermissionError:
            print("You do not have permission.")
    else:
        print("SERVER_FILE is not set.")


def validate_server(item):
    if type(item) == dict:
        if "name" in item and "status" in item and "cpu" in item:
            if type(item['name']) == str and type(item['status']) == str and type(item['cpu']) == int:
                if item['status'] == 'online' or item['status'] == 'offline':
                    if item['cpu'] >= 0 and item['cpu'] <= 100:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False

