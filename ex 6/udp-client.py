import socket

HOST = "localhost"
PORT = 55555
BUFFER = 1024

c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
c.settimeout(30)

try:
    while True:
        msg = input("CLIENT: ")
        if msg == "quit":
            break
        
        c.sendto(bytes(msg,"utf-8"), (HOST, PORT))
        
        data, addr = c.recvfrom(BUFFER)
        print("SERVER: {}".format(data.decode("utf-8")))
        
except Exception as e:
    print(e)
    
finally:
    c.close()
    print("e")
        
    






