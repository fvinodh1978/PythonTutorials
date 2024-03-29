import json
import math
import os
import re
from itertools import count
from pathlib import Path


def format_json(feed_file):
    data = None
    with open(feed_file, "r") as file:
        data = json.load(file)
    file.close()
    # with open("C:\Official\ELK\Data\Processed\PhysicalEquipment_UIV_20220908_0045.json", "w") as f:
    #     f.write('{}\n '.format(json.dumps(data)))
    # f.close()

    with open("C:\Official\ELK\Data\Processed\PhysicalEquipment_UIV_20220908_0045.json", "w") as f:
        json.dump(data, f)
        f.write('\n')
    f.close()


def add_newline(feed_file):
    data = None
    with open(feed_file, "r") as file:
        data = file.read()
    file.close()
    # search_text = "^\s{2,}"
    search_text = "\n"
    replace_text = ""
    data = data.replace(search_text, replace_text)
    with open("C:\Official\ELK\Data\Processed\PhysicalEquipment_UIV_20220904_0045.json", "w") as f:
        f.write(data + "\n")
        # f.write('{}\n'.format(json.dumps(data)))
    f.close()


def clean_dict(feed_file):
    with open(feed_file, "r") as file:
        data = file.read()
    file.close()
    # search_text = "^\s{2,}"
    search_text = "\n"
    replace_text = ""
    data = data.replace(search_text, replace_text)
    with open("C:\Official\ELK\Data\Processed\CNF_UIV_20220904_0045.json", "w") as file:
        file.write(data)
    # print(data)
    file.close()


def split_json_array(file):
    docs = json.load(open(file))
    # my_file = os.path.basename(file)
    my_file = Path(file).resolve().stem
    my_path = os.path.dirname(file)
    print(my_path, my_file)
    file_path = "C:\Official\ELK\Data\Processed\\" + my_file
    for ii, doc in enumerate(docs):
        with open(file_path + "_" + '{}.json'.format(ii), 'w') as out:
            # json.dump(doc, out)
            out.write('{}\n\r'.format(json.dumps(doc)))


def render_files_to_logstash():
    files = []
    file_path = "C:\Official\ELK\Data\Processed"
    files = [os.path.join(file_path, f) for f in os.listdir(file_path) if os.path.isfile(os.path.join(file_path, f))]
    for file in files:
        print(file)


def count_records(file_name):
    with open(file_name, 'r') as JSONFile:
        data = json.load(JSONFile)
    count = 0
    for obj in data:
        count = count + 1
        print(count, obj['globalName'])
    return count


def get_chunk_size(file_name, size):
    print(f"*******File Type *********" + file_name)
    physical_file_size = 10
    chunk_size = 0
    if file_name == "PhysicalEquipment":
        chunk_size = size // physical_file_size
    elif file_name == "CNF":
        chunk_size = (size // physical_file_size) + 1
    elif file_name == "VNF":
        chunk_size = (size // physical_file_size) + 1
    elif file_name == "Organization":
        chunk_size = (size // physical_file_size) + 1
    else:
        print(f"*******Invalid File Type *********")
    return chunk_size


def split_file(file_name):
    extracted_dir_path = "C:\\Official\\Projects\\CloudBand\\Data\\Prod\\UIV_20230819_0045"
    physical_file_size = 10
    out_path = extracted_dir_path
    with open(os.path.join(extracted_dir_path, file_name), 'r') as f1:
        data = json.load(f1)
        size = len(data)

    file = Path(os.path.basename(file_name)).resolve().stem
    chunk_size = math.ceil(size / physical_file_size)

    num_file = 0
    for i in range(0, len(data), chunk_size):
        num_file = num_file + 1
        json.dump(data[i:i + chunk_size], open(out_path + '/' + file + "_" + str(i) + '.json', 'w', encoding='utf8'),
                  ensure_ascii=False,
                  indent=True)
    os.remove(os.path.join(extracted_dir_path, file_name))
    print(file_name + " : Size : " + str(size) + " chunk_size " + str(chunk_size) + " , Splited into " + str(
        num_file) + " Files")


def get_json_obj(my_file, outfile, key, value):
    with open(my_file, 'r') as file_obj:
        python_obj = json.load(file_obj)
        print("Total Records : " + str(len(python_obj)))
    filtered_list = [
        dictionary for dictionary in python_obj
        if (dictionary[key] == value)
    ]
    print(str(len(filtered_list)) + " : " + str(type(filtered_list)))
    with open(outfile, "w") as outfile_obj:
        json.dump(filtered_list, outfile_obj)


def split_file(file_name):
    extracted_dir_path = "C:\\Official\\Projects\\CloudBand\\Data\\Prod\\UIV_20230820_0045"
    physical_file_size = 10
    out_path = extracted_dir_path

    if "PhysicalLink_UIV" not in file_name:
        with open(os.path.join(extracted_dir_path, file_name), 'r') as f1:
            data = json.load(f1)
            size = len(data)

        file = Path(os.path.basename(file_name)).resolve().stem
        chunk_size = math.ceil(size / physical_file_size)

        num_file = 0
        for i in range(0, len(data), chunk_size):
            num_file = num_file + 1
            json.dump(data[i:i + chunk_size],
                      open(out_path + '/' + file + "_" + str(i) + '.json', 'w', encoding='utf8'),
                      ensure_ascii=False,
                      indent=True)
        os.remove(os.path.join(extracted_dir_path, file_name))
        print(file_name + " : Size : " + str(size) + " chunk_size " + str(chunk_size) + " , Splited into " + str(
            num_file) + " Files")
    print(f"*******Leaving split_json_files *********")


def get_obj_count(my_file):
    with open(my_file, "r") as file_obj:
        python_obj = json.load(file_obj)
    print("Total Records : " + str(len(python_obj)))


def get_ip_count(my_file, out_file):
    # my_file=os.path.abspath("../../Resources/ip_file.txt")
    with open(my_file, "r") as file_obj:
        file_content = file_obj.read()
    ips = re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', file_content)
    print("Number of Ips :", len(ips))

    # for ip in ips:
    #     print(ip)

    with open(out_file, "w") as out_file_obj:
        out_file_obj.write('\n'.join([i for i in ips[0:]]))

    # print("Octects :", octects)


def get_key_value_count(my_path, key):
    files = os.listdir(my_path)
    for file in files:
        my_file = os.path.join(my_path, file)
        kinds = []
        with open(my_file, "r") as file_obj:
            for line in file_obj:
                # items = re.findall("\"" + key + "\"\s*:\s*\"*[a-z, A-Z, 0-9]*\"*", line)
                items = re.findall("\"" + key + "\"\s*:\s*\"*.+\"*", line)
                # print(items)
                for item in items:
                    kinds.append(str(item.replace('"', "").split(":")[1].strip()))
        for kind in set(kinds):
            print(file + " : " + kind + " : " + str(kinds.count(kind)))


def get_file_type():
    file_suffix = ".json"
    files = ["PhysicalEquipment_UIV" + file_suffix,
             "Organization_UIV" + file_suffix,
             "CNF_UIV" + file_suffix,
             "VNF_UIV" + file_suffix,
             "PhysicalLink_UIV" + file_suffix]
    for file in files:
        file_type = file.split("_")[0]
        print(file_type)


def get_json_obj_count(file_name):
    extracted_dir_path = "C:\\Official\\Projects\\CloudBand\\Data\\Prod\\UIV_20230822_0045"
    if "PhysicalLink_UIV" in file_name:
        with open(os.path.join(extracted_dir_path, file_name), 'r') as f1:
            data = json.load(f1)
            data = data.get("content")
            size = len(data)
    if "PhysicalLink_UIV" not in file_name:
        with open(os.path.join(extracted_dir_path, file_name), 'r') as f1:
            data = json.load(f1)
            size = len(data)
    print(file_name + " : Number of json Objects : " + str(size))


def split_file1(file_name):
    extracted_dir_path = "C:\\Official\\Projects\\CloudBand\\Data\\Prod\\UIV_20230820_0045"
    physical_file_size = 10
    out_path = extracted_dir_path
    print("Processing : " + file_name)
    with open(os.path.join(extracted_dir_path, file_name), 'r') as f1:
        data = json.load(f1)
        if "PhysicalLink_UIV" in file_name:
            data = data.get("content")
        size = len(data)

    file = Path(os.path.basename(file_name)).resolve().stem
    chunk_size = math.ceil(size / physical_file_size)
    temp_dict = {}
    num_file = 0
    for i in range(0, len(data), chunk_size):
        num_file = num_file + 1
        content = data[i:i + chunk_size]
        if "PhysicalLink_UIV" in file_name:
            temp_dict["content"] = content
            content=temp_dict
        json.dump(content, open(out_path + '/' + file + "_" + str(i) + '.json', 'w', encoding='utf8'),
                  ensure_ascii=False,
                  indent=True)
    os.remove(os.path.join(extracted_dir_path, file_name))
    print(file_name + " : Size : " + str(size) + " chunk_size " + str(chunk_size) + " , Splited into " + str(
        num_file) + " Files")

print(f"*******Leaving split_json_files *********")

# get_file_type()

# file = "C:\Official\Projects\CloudBand\Data\Prod\\UIV_20230819_0045\PhysicalEquipment_UIV_20230819_0045.json"
# split_file(file)
# file = "C:\Official\Projects\CloudBand\Data\Prod\\UIV_20230819_0045\VNF_UIV_20230819_0045.json"
# split_file(file)
# file = "C:\Official\Projects\CloudBand\Data\Prod\\UIV_20230819_0045\CNF_UIV_20230819_0045.json"
# split_file(file)

files = ["PhysicalEquipment_UIV",
         "Organization_UIV",
         "CNF_UIV",
         "VNF_UIV",
         "PhysicalLink_UIV"]
extracted_dir_path = "C:\\Official\\Projects\\CloudBand\\Data\\Prod\\UIV_20230820_0045"
fileList = os.listdir(extracted_dir_path)

print("=====================================")
fileList = os.listdir(extracted_dir_path)
filesTobeProcessed = []

for file_name in fileList:
    for temp_file in files:
        if temp_file in file_name:
            filesTobeProcessed.append(file_name)
print(filesTobeProcessed)
for file in filesTobeProcessed:
    # get_json_obj_count(file)
    split_file1(file)
