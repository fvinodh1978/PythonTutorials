import json
import os.path

try:
    json_str = '{"abc":"abc"}'
except FileNotFoundError as e:
    print("File doesnt exists in the folder...")
else:
    python_dict = json.loads(json_str)
    json_str = json.dumps(python_dict)
    print(json_str, type(json_str))
