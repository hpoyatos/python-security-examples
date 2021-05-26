import socket

def portscanner(port):
    if sock.connect_ex((host,port)) == False:
        print("Porta {} aberta".format(port))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(1)

host = input("[*] Digite o host para escanear: ")

for port in range(1,100):
    portscanner(port)