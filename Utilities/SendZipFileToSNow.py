# Need to install requests package for python
import json
import requests

def publish_file(url, input_file):
    # url = 'https://dev145312.service-now.com/api/x_573775_sndatam_0/snow_migration_service/SendFilesToSnow?table_name=x_573775_sndatam_0_snow_migration_audit&table_sys_id=802287541b6e1d50f1a897d7bd4bcbe6&file_name=rack_data.json&feed_name=Site'
    #url = 'https://dev145312.service-now.com/api/x_573775_sndatam_0/snow_migration_service/SendZipFileToSnow?file_name=site_file.zip&table_name=x_573775_sndatam_0_snow_transaction_log'

    # data = open(input_file, 'rb').read()

    data = {
        'comment': 'Load Location Data10',
        'feed_name': 'Site',
        'status': 'ready',
        'download_link': 'abc',
        'rec_sysid': 'abc',
        'file_name': 'a',
        'table_name': 'aba'
    }

    #nonprod uid/pwd
    user = 'm51355'
    pwd = 'CFXuKd*k=e8%ZnGH?HMz1]%IW((hGLo@{jE]3!j('

    headers = {"Content-Type": "application/json", "Accept": "application/json"}

    # Do the HTTP request
    response = requests.post(url, auth=(user, pwd), headers=headers, data=json.dumps(data))
    # response = requests.post(url, auth=(user, pwd), headers=headers, data=data)
    outdata = json.dumps(response.json(), indent=4)
    print(outdata)

#Personal Instance
# url='https://dev145312.service-now.com/api/x_573775_sndatam_0/snow_migration_service/SendZipFileToSnow?file_name=site_file.zip&table_name=SNow Transaction Log'
# url='https://dev145312.service-now.com/api/x_573775_sndatam_0/snow_migration_service/SendZipFileToSnow?file_name=site_data.json&table_name=SNow Transaction Log&feed_name=Site'
# input_file = 'C:\\Personal\\MyProjects\\ServiceNow\\Data\\pi\\site_data.json'

#Non Prod
# Site
input_file='C:\\Personal\\MyProjects\\ServiceNow\\Data\\att\\site_lab.zip'
url='https://attdistdev2.service-now.com/api/x_att2_cloudband_u/ams_snow_migration_service/publish_cb_file?file_name=site_lab.zip&table_name=x_att2_cloudband_u_ams_snow_staging&feed_name=site'

#Space
input_file = 'C:\\Personal\\Vinodh\\MyProjects\\PythonProjects\\Workspace\\Resources\\site_file.zip'
url = 'https://attcommdev4.service-now.com/api/x_att2_cloudband_u/ams_snow_migration_service/publish_cb_file?file_name=space_lab.zip&table_name=x_att2_cloudband_u_ams_snow_staging&feed_name=rack'

#Physical Device
# input_file = 'C:\\Personal\\Vinodh\\MyProjects\\PythonProjects\\Workspace\\Resources\\site_file.zip'
# url = 'https://attdisttest2.service-now.com/api/x_att2_cloudband_u/ams_snow_migration_service/publish_cb_file?file_name=site_file.zip&table_name=x_att2_cloudband_u_ams_snow_staging&feed_name=PhysicalDevice'

#Physical Port
# input_file = 'C:\\Personal\\MyProjects\\ServiceNow\\Data\\att\\physical_port_lab.zip'
# url = 'https://feed_name=PhysicalDevice/api/x_att2_cloudband_u/ams_snow_migration_service/publish_cb_file?file_name=physical_port_lab.zip&table_name=x_att2_cloudband_u_ams_snow_staging&feed_name=PhysicalPort'

publish_file(url, input_file)