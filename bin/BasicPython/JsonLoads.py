import json

# Script to convert json file to Python Dictionary
try:
    json_str = '{"abc":"abc"}'
    json_str = '''{"abc":"abc", 
    "lmn":"lmn"
    }'''
except FileNotFoundError as e:
    print("File doesnt exists in the folder...")
else:
    python_dict = json.loads(json_str)
    for key, value in python_dict.items():
        print(key, value)
