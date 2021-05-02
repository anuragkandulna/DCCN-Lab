import socket
from sys import exit
from os import getcwd

# create client socket and configure it
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.settimeout(120)

# set default host and port number
HOST = 'localhost'  
PORT = 9999  
BUFFER = 1024
FILE_NAME = "index.html"


# try to connect to server using default values
try:
    c.connect((HOST, PORT))
except Exception as e:
    print(e)
    exit()


def download_file():
    """
    Stream bytes from server
    """
    data = c.recv(BUFFER)
    
    if data == b"terminate":
        print("DOWNLOADING FAILED !!!")
        return

    file = open(FILE_NAME,"wb")
    while True:
        if data == b"DONE":
            break
        
        print("Receiving. . . ")
        file.write(data)
        data = c.recv(BUFFER)
    
    file.close()
    print("Successfully received!!!")
    
    print("Webpage saved as {} at {}".format(FILE_NAME, getcwd()))    
    return None


# communicate with server
try:    
    ack = c.recv(BUFFER)
    print(ack.decode("utf-8"))

    data_url = input("Enter a vaild URL: ")
    c.send(bytes(data_url,"utf-8"))
        
    download_file()
    
except Exception as e:
    print(e)
    
finally:
    c.close()
    print("EXITING !!!")
    


