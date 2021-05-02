import socket
import pycurl
from sys import exit
from io import BytesIO
from os import path, remove, stat, getcwd

# create and configure socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(120)  

# set default host and port number
HOST = 'localhost'  
PORT = 9999 
STR = "Welcome to website downloader!"
BUFFER = 1024
FILE_NAME = "local.html"
TEMP_FILE = "{}/{}".format(getcwd(), FILE_NAME)


def web_downloader(my_url):
    """
    Download webpage and stream to client
    """
    
    buffer = BytesIO()
    obj = pycurl.Curl()
    try:
        
        obj.setopt(obj.URL, my_url)
        obj.setopt(obj.WRITEDATA, buffer)
        obj.perform()
        obj.close()
    except:
        print("ERROR")
        
    body = buffer.getvalue()
    
    # TEMP_FILE = "{}/{}".format(getcwd(), FILE_NAME)
    file = open(TEMP_FILE,"wb")
    file.write(body)
    file.close()
    
    
    fsize = stat(TEMP_FILE).st_size
    if fsize > 0:
        print("Webpage saved in local directory.")
    else :
        remove(TEMP_FILE)
        print("FILE SAVING ERROR")
        
    return None
 
    
def file_streamer(my_file):
    """
    Upload local file to server
    """
    # client.send(bytes("terminate","utf-8"))
    # return

    if not path.isfile(my_file):
        print("FILE NOT FOUND in local directory. \n")
        client.send(bytes("terminate","utf-8"))
        return
    
    
    # c.send(bytes(file_name,"utf-8"))
    file = open(my_file, "rb")
    data = file.read(BUFFER)
    while data:
        print("Sending. . .")
        client.send(data)
        data = file.read(BUFFER)
    else:
        print("Sent successfully !!!")    
    file.close()
    client.send(b"DONE")
    
    return None


try:
    s.bind((HOST, PORT))
except Exception as e:
    print(e)
    exit()

# start server
s.listen()
print("WAITING FOR CLIENT. . . ")


# communicate with client
try:
    while True:
        client, addr = s.accept()
        client.send(bytes(STR,"utf-8"))
        print('Connected with {} \n'.format(addr))
        
        recv_url = client.recv(BUFFER)
        recv_url = recv_url.decode("utf-8")
        
        web_downloader(recv_url)
        
        file_streamer(FILE_NAME)

        # client.close()
        
except Exception as e:
    print(e)
finally:
    client.close()
    s.close()
    print("EXITING !!!")     

