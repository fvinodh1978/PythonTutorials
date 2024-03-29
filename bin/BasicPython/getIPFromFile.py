import json
import os.path
import re
def get_ip_count():
    my_file=os.path.abspath("../../Resources/ip_file.txt")
    with open(my_file, "r") as file_obj:
        file_content = file_obj.read()
    ips = re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', file_content)
    octects = set()
    for ip in ips:
        octect = re.findall(r'(^\d{1,3})', ip)
        octects.add(octect[0])
    # print("IPs :", ips)
    print("Number of Ips :", len(ips))
    # print("Octects :", octects)
def get_rec_count(search_str):
    print("Number of Ips :")

def get_json_obj():

    json_array = json.dumps(
        [
            {'name': 'Alice', 'salary': 100},
            {'name': 'Bobby', 'salary': 50},
            {'name': 'Carl', 'salary': 75}
        ]
    )

    a_list = json.loads(json_array)

    filtered_list = [
        dictionary for dictionary in a_list
        if dictionary['salary'] > 50
    ]

    # 👇️ [{'name': 'Alice', 'salary': 100}, {'name': 'Carl', 'salary': 75}]
    print(filtered_list)
get_json_obj()