#！/usr/bin/python3
import requests
import sys


values = {
    'mesConSubject': 'hahah',
    'mesConBody': 'test',
    'mesRecipentNameList': ['uzhat110'],
    'mesSendName': "uliue007",
    'sendMessageType': 2,
    'systemName': "zabbix"
    }
response = requests.post('http://172.28.14.198:18083/message/sendMessage',json=values)
print("status code:",response.status_code)
print(response.json())