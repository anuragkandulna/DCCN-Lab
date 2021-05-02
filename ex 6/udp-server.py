import socket
from sys import exit

HOST = "localhost"
PORT = 55555
BUFFER = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.settimeout(60)

try:
    s.bind((HOST, PORT))
except Exception as e:
    print(e)
    exit()


print("UDP server is started. . . ")


try:
    while True:
        data, addr = s.recvfrom(BUFFER)
        if data.decode("utf") == "quit":
            break
        
        print("CLIENT {}: {}".format(addr, data.decode("utf-8")))
        
        msg = input("SERVER: ")
        s.sendto(bytes(msg,"utf-8"), addr)
        
except Exception as e:
    print(e)
    
finally:
    s.close()
    print("e")

