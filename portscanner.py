import socket
from IPy import IP

def banner_info(s):
    print(str(s.recv(1024).decode().strip('\n')))
    return s.recv(1024)

def checkip(ip):
    try:
        IP(ip)
        return ip
    except ValueError:
        return ip


def portscan(ip,port):
    try:
        sock = socket.socket()
        sock.settimeout(1)
        sock.connect((ip, port))
        try:
            ban = banner_info(sock)
            print('[+] The Port ' + str(port) + 'is open and details are' + str(ban) + '')
        except:
            print('[+] The Port ' + str(port) + 'is open no details')
    except:
        pass

ip = input('[+] Enter your targeted ip:')
valip = checkip(ip)

for port in range(1,100):
    portscan(valip, port)