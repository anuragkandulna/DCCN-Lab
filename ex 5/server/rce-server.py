import socket
import subprocess
from os import getcwd
from sys import exit

HOST = "localhost"
PORT = 55555
BUFFER = 1024
FILE_NAME = "temp.bat"

# create and configure server socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.settimeout(60)

try:
    s.bind((HOST, PORT))
    print("Waiting for connection. . . ")
except Exception as exception:
    print(exception)
    exit()


try:    
    while True:
        data, client_ip = s.recvfrom(BUFFER)
    
        print("Command received from {}: {}".format(client_ip, data.decode()))
    
        file = open(FILE_NAME,"w")
        # loc = getcwd()
        file.write("{}".format(data.decode()))
        file.close()
    
        print("Processing request. . .\n")
        P = subprocess.run([r"{}\{}".format(getcwd(), FILE_NAME)],
                           capture_output=True,
                           shell=True,
                           check=True)
    
        # save output to dictionary
        DICT = {"inp": P.args,
                "ret": P.returncode,
                "opt": P.stdout.decode(),
                "err": P.stderr.decode(),
                "chkcode": P.check_returncode()}
    
    
        print("INPUT: {} \n".format(DICT["inp"]))
        print("RETURN: {} \n".format(DICT["ret"]))
        print("OUTPUT: {} \n".format(DICT["opt"]))
        print("ERROR: {} \n".format(DICT["err"]))
        print("RETURN CODE: {} \n".format(DICT["chkcode"]))    

        # return output back to client
        s.sendto(bytes(DICT["opt"],"utf-8"), client_ip )
        print("Request Completed !!!")
    
except Exception as exception:
    print(exception)
    
finally:
    s.close()
    print("Exiting !!!")
    exit()
    