import socket
import threading
import requests




Message_Api = {
    'mesConSubject': '172.28.13.140 Server port Unavailable',
    'mesConBody': '',
    'mesRecipentNameList': ['uzhat110'],
    'mesSendName': "uliue007",
    'sendMessageType': 2,
    'systemName': "zabbix"
    }

lock = threading.Lock()
Num = 0
threads = []
# Message_Api['mesConBody'] = ''
with_error = False


def port_scanner(host, port):
    global Num
    global with_error
    try:
        s = socket.socket()
        s.connect((host, port))
        lock.acquire()
        Num += 1
        print('%d open' % port)
        lock.release()
        s.close()
    except Exception as e:
        with_error = True
        Message_Api['mesConBody'] = Message_Api['mesConBody'] + " " + str(port)  ##邮件内容
        print("%d port Unavailable" % port)
        print(e)

def main():
    for p in range(22, 24):
        t = threading.Thread(target=port_scanner, args=('172.28.13.140', p))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    if with_error == True:
        response = requests.post('http://172.28.13.134:18083/message/sendMessage', json=Message_Api)
        print("status code:", response.status_code)
        print(response.json())
        print('IS COMPLETE')
        print('%d open port' %  (Num))
        Message_Api['mesConBody'] = ''


if __name__ == '__main__':
    main()
