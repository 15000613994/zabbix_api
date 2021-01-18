import socket

IPs = ['127.0.0.1', '172.28.13.140']
Ports = [21, 80, 8080]

for ip in IPs:
    for port in Ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3)
        result = s.connect_ex((ip, port))
        if result == 0:
            print("The Server IP: {} , Port {} has been used".format(ip, port))
            print(result)
        elif result == 10061:
            print("The Server IP: {} , Port {} not enabled".format(ip, port))
            print(result)
        elif result == 10035:
            print("The Server IP: {} , no response".format(ip, port))
            print(result)
        else:
            print(result)
        s.close()