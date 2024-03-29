import json
import os.path
from io import UnsupportedOperation


class MyProject:
    def get_env(self, env_param):
        my_File = os.path.abspath("..\..\Resources\env_properties.json")
        with open(my_File, "r") as file_obj:
            json_object = json.load(file_obj)
            return json_object.get(env_param)

    def set_env(self, key, value):
        from json import JSONDecodeError
        try:
            my_file = os.path.abspath("..\..\Resources\env_properties1.json")
            with open(my_file, "r") as file_obj:
                json_object = json.load(file_obj)
                json_object[key] = value

        except (FileNotFoundError, JSONDecodeError) as e:
            env_data = '{"' + key + '":"' + value + '"}'
            json_object = json.loads(env_data)
            with open(my_file, "w") as file_obj:
                json.dump(json_object, file_obj)
            print(json_object)

            print("Please check if file is Present")

        else:

            return json_object
        finally:
            file_obj.close()
            print("Processing Complete")


myCar = MyProject()
print(myCar.get_env("browser"))
print("New Browser is ", myCar.set_env("browser", "ff"))
