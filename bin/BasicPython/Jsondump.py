import json

#Script to convert json file to Python Dictionary

file= "/PythonTutorials/Resources/site_file.json"
try:
    file_obj = open(file, "r")
except FileNotFoundError as e:
    print("File doesnt exists in the folder...")
else:
    python_dict = json.load(file_obj)
    for key in python_dict[0].keys():
        print(python_dict[0].get(key))
file_obj.close()

#Script to convert json String(from File) to Python Dictionary
try:
    file_obj = open(file, "r")
except FileNotFoundError as e:
    print("File doesnt exists in the folder...")
else:
    python_dict = json.loads(file_obj.read())
    for key in python_dict[0].keys():
        print(python_dict[0].get(key))

#Script to convert raw json String sinle-line or multi-line to Python Dictionary
try:
    # json_str = '[{"feed_name": "device","status": "ready1","total_records": "100","records_inserted": "30"}]'
    json_str='''[
    {
        "feed_name": "device",
        "status": "ready1",
        "total_records": 100,
        "records_inserted": 30,
        "records_updated": 50,
        "records_failed": 20,
        "failure_reason": "Unique Constraint",
        "download_link": "",
        "table": "x_573775_sndatam_0_snow_transaction_log",
        "comment": "Load Device Data1"
    }
]'''
except FileNotFoundError as e:
    print("File doesnt exists in the folder...")
else:
    python_dict = json.loads(json_str)
    for key in python_dict[0].keys():
        print(python_dict[0].get(key))
