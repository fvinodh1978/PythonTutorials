import re


def sum(*args):
    sum = 0
    for i in range(len(args)):
        sum += args[i]
    return sum


def getIpFromText(text):
    ips = re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', text)
    return ips
