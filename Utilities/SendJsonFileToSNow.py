# Need to install requests package for python
import json
import requests

# url = 'https://dev145312.service-now.com/api/x_573775_sndatam_0/snow_migration_service/SendFilesToSnow?table_name=x_573775_sndatam_0_snow_migration_audit&table_sys_id=802287541b6e1d50f1a897d7bd4bcbe6&file_name=rack_data.json&feed_name=Site'
url = 'https://dev145312.service-now.com/api/x_573775_sndatam_0/snow_migration_service/SendJsonFileToSnow?file_name=site_file.json'
data = open('C:\\Personal\\MyProjects\\PythonProjects\\Workspace\\Resources\\site_file.json', 'rb').read()

# Eg. User name="admin", Password="admin" for this code sample, and headers
user = 'admin'
pwd = 'Iis0slCB=+K2'
headers = {"Content-Type": "application/json", "Accept": "application/json"}

# Do the HTTP request
response = requests.post(url, auth=(user, pwd), headers=headers, data=data)
outdata = json.dumps(response.json(), indent=4)
print(outdata)
