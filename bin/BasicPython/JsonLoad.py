import json
import os.path

# Script to convert json file to Python Dictionary - json.load()

my_File = os.path.abspath("../../Resources/site_file.json")
try:
    file_obj = open(my_File, "r")
except FileNotFoundError as e:
    print("File doesnt exists in the folder...")
else:
    python_dict = json.load(file_obj)
    for key, value in python_dict[0].items():
        print(key, " ", value)
file_obj.close()
