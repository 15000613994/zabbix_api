import socket
import threading
import requests


threads = []
IPs = ['127.0.0.1', '172.28.13.140']
Ports = [21, 80, 8080]


def port_scanner(IPs, Ports):
        for ip in IPs:
            for port in Ports:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(3)
                result = s.connect_ex((ip, port))
                if result == 0:
                    print("The Server IP: {} , Port {} has been opend".format(ip, port))
                    # print(result)
                elif result == 10061:
                    print("The Server IP: {} , Port {} not Unavailable".format(ip, port))
                    # print(result)
                elif result == 10035:
                    print("The Server IP: {} , no response".format(ip, port))
                    # print(result)
                else:
                    print(result)
                s.close()

def main():
        for p in range(3):
            t = threading.Thread(target=port_scanner, args=(IPs, Ports))
            threads.append(t)
            t.start()
        for t in threads:
            t.join()



if __name__ == '__main__':
    main()



