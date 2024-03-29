import json

import requests

# cookies = {
#     'SESSID': 'ABCDEF',
# }

cookies = {}

headers = {
    'Connection': 'keep-alive',
    'Accept-Encoding': 'gzip, deflate, br, zip',
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

user = 'admin'
pwd = 'Iis0slCB=+K2'

data = open('C:\\Personal\\MyProjects\\PythonProjects\\Workspace\\Resources\\site_file.json', 'rb').read()

url = 'https://dev145312.service-now.com/api/x_573775_sndatam_0/snow_migration_service/SendZipFileToSnow1?file_name=site_file.zip '
response = requests.post(url, auth=(user, pwd), headers=headers, cookies=cookies, data=data)
outdata = json.dumps(response.json(), indent=4)
print(outdata)