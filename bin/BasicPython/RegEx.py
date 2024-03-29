import re

text = "Yesterday 12.22.121.9 there was a Rain in 12.22.121.10 Spain for 135.220.121.10 days"
x = re.sub("ain", "9", text)
print(x)
x = re.split("\s", text)
print(x)
# x= re.findall("[1-9].?[1-9].?[1-9].?[1-9]", text)
ips = re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', text)
myips = set()
for ip in ips:
    octect=re.findall(r'(^\d{1,3})', ip)
    myips.add(octect[0])
print(myips)
