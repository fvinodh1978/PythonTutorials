# Need to install requests package for python
# easy_install requests
import json

import requests

# Request Docs: http://docs.python-requests.org/en/master/user/quickstart/
#Delete the attachment
attach_sysid='671243141b6e1d50f1a897d7bd4bcb06'
attach_del_url='https://dev145312.service-now.com/api/now/attachment'
#https://dev76341.service-now.com/api/now/attachment/671243141b6e1d50f1a897d7bd4bcb06
# Set the request parameters
url = 'https://dev145312.service-now.com/api/now/attachment/file?table_name=x_573775_sndatam_0_snow_migration_audit&table_sys_id=802287541b6e1d50f1a897d7bd4bcbe6&file_name=rack_data.zip&feed_name=Site'
# url = 'https://fejr5sb8ead6.runscope.net/api/now/attachment/file?table_name=incident&table_sys_id=81f8915bdb6ba20028927416bf961971&file_name=issue_screenshot'
# url = 'https://dev76341.service-now.com/api/now/attachment/file?table_name=sys_data_source&table_sys_id=46ad6ed01b2e1d50f1a897d7bd4bcb17&file_name=snow_audit1'
# specify files to send as binary
data = open('C:\\Personal\\MyProjects\\ServiceNow\\Data\\rack_data.zip', 'rb').read()

# Eg. User name="admin", Password="admin" for this code sample.
user = 'admin'
pwd = 'Iis0slCB=+K2'

# Set proper headers
headers = {"Content-Type": "application/json", "Accept": "application/json"}

# Do the HTTP request
response = requests.post(url, auth=(user, pwd), headers=headers, data=data)

# Check for HTTP codes other than 200
# if response.status_code != 200:
#     print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
#     exit()

# Decode the JSON response into a dictionary and use the data
data = json.dumps(response.json(), indent=4)
# sys_id = response.json()['result']['sys_id']
# url = 'https://dev76341.service-now.com/api/now/attachment/' + sys_id
# response = requests.get(url, auth=(user, pwd), headers=headers)
# data = json.dumps(response.json(), indent=4)
print(data)
sys_id = response.json()['result']['sys_id']
download_link = response.json()['result']['download_link']
file_name = response.json()['result']['file_name']
table_name= response.json()['result']['table_name']
data = {
    'comment': 'Load Location Data10',
    'feed_name': 'Site',
    'status': 'ready',
    'download_link': download_link,
    'rec_sysid': sys_id,
    'file_name': file_name,
    'table_name': table_name
}

url = 'https://dev145312.service-now.com/api/now/table/x_573775_sndatam_0_snow_migration_audit/802287541b6e1d50f1a897d7bd4bcbe6'
response = requests.patch(url, auth=(user, pwd), headers=headers, data=json.dumps(data))
print(json.dumps(response.json(), indent=4))
