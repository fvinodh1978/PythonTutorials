import json
import os

my_File = os.path.abspath("../../Resources/out_file.json")
try:
    file_obj = open(my_File, "a")
except (FileNotFoundError) as e:
    print("File doesnt exists in the folder...")
else:
    # json_obj = json.dumps(python_obj)
    file_obj.write("\nThis is New End!")
finally:
    print("File Writing Completed")
    file_obj.close()
    file_obj = open(my_File, "r")
    print(file_obj.read())
