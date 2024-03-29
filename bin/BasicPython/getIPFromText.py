import os.path
import re
text = "Yesterday 12.22.121.9 there was a Rain in 12.22.121.10 Spain for 135.220.121.10 days"
ips = re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', text)
octects = set()
for ip in ips:
    octect = re.findall(r'(^\d{1,3})', ip)
    octects.add(octect[0])
print("IPs :", ips)
print("Octects :", octects)