import socket
from os import path
from sys import exit

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(60)
    
# set default host and port number
HOST = 'localhost'  
PORT = 9999 
BUFFER = 1024
STR = """Available choices: 
1. Upload to server 
2. Download from server
3. Type 'quit' to exit
"""


# bind port number to the host
try:
    s.bind((HOST, PORT))
except Exception as e:
    print(e)
    exit()
    
# listen for connections
s.listen()
print("WAITING FOR CLIENT. . . ")

try:
    client, addr = s.accept()
except Exception as e:
    print(e)
    exit()
    
def file_write(file_name):
    """
    Write file to current working directory
    """
    
    print("WRITE MODE SELECTED")
    file_name = file_name.decode("utf-8")
    
    if file_name == "terminate":
        print("TERMINATED")
        return
    
    if path.isfile(file_name):
        file_name = "_duplicate_{}".format(file_name)
        print("DUPLICATE FILE RECEIVED. FILE RENAMED.")
    
    file = open(file_name,"wb")    
    while True:
        data = client.recv(BUFFER)
        if data == b"DONE":
            print("File successfully received")
            break
        print("Receiving. . . ")
        file.write(data)
        
    file.close()
    print("SUCCESS\n")
    
    
def file_read(file_name):
    """
    Read file from  current working directory
    """
    
    print("READ MODE SELECTED")
    file_name = file_name.decode("utf-8")
    
    if not path.isfile(file_name):
        print("FILE NOT FOUND in local directory. \n")
        client.send(bytes("terminate","utf-8"))
        return None
    
    client.send(bytes(file_name,"utf-8"))
    file = open(file_name, "rb")
    data = file.read(BUFFER)
    
    while data:
        print("Sending. . .")
        client.send(data)
        data = file.read(BUFFER)
    else:
        print("Upload successful!!! ")
        
    file.close()
    client.send(b"DONE")
    print("SUCCESS\n")
    
    
def main():
    try:
        client.send(bytes("WELCOME TO FILE SERVER:\n {}".format(STR),"utf-8"))
        print("Connected with {} \n".format(addr))
    except Exception as e:
        print(e)
        return
    
    while True:
        opt = client.recv(BUFFER)
        opt = opt.decode("utf-8")
        
        if opt == "1":
            print("Option 1 selected")
            file_name = client.recv(BUFFER)
            file_write(file_name)   
        elif opt == "2":
            print("Option 2 selected")
            file_name = client.recv(BUFFER)
            file_read(file_name) 
        elif opt == "quit":
            print("Client selected Quit \n")
            break;
        else:
            print("Wrong choice !!!")
    
    client.close()
    print("CLIENT DISCONNECTED !!!")
    s.close()
    print("EXITING !!!")
        

if __name__=="__main__": main()
        