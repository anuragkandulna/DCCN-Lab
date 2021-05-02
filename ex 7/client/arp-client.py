import socket
from sys import exit
from ipaddress import ip_address


HOST = "localhost"
PORT = 55555
BUFFER = 1024


c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
c.settimeout(30)

ip = input("Enter a valid IP-address: ")

try:
    ip_address(ip)
except:
    print("Invalid IP")
    exit()


try:
    c.sendto(bytes(ip,"utf-8"), (HOST, PORT))
except Exception as exception:
    print(exception)
    c.close()
    exit()


try:
    msg, ip = c.recvfrom(BUFFER)
    print("RECEIVED: {} \n".format(msg.decode()))
except Exception as exception:
    print(exception)
finally:
    c.close()
    print("Exiting !!!")
    exit()

