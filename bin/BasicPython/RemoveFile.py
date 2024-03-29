import os.path

file="C:\Personal\Vinodh\MyProjects\PythonProjects\Workspace\PythonTutorials\Resources\createfile.txt"
try:
    file_exists = os.path.exists(file)
    if not file_exists:
        raise FileNotFoundError("File is not found")
except TypeError as e:
    print("File doesnt exists in the folder...")
else:
    os.remove(file)
finally:
    print("File Processing Completed")
