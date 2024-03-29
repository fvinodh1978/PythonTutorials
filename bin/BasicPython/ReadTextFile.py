import json
import os

my_File = os.path.abspath("../../Resources/site_file.json")
try:
    file_obj = open(my_File, "r")
except (FileNotFoundError) as e:
    print("File doesnt exists in the folder...")
else:
    lines = file_obj.readlines()
    for line in lines:
        print(line, end=" ")
finally:
    print("File Reading Completed")
    file_obj.close()
