from sys import exit

while True:
    print(""" 
          Choices (Type exit in terminal to exit):
          1. Get file from server 
          2. Put file into server 
          """)
    choice = input("Enter your input: ")
    
    if choice == "exit":
        exit()
    elif choice == "1":
        print("GET")
        file_name = input("Enter file name: ")
    elif choice == "2":
        print("PUT")
        file_name = input("Enter file name: ")
    else:
        print("Wrong choice!!!")

            

# import os

# FILE_NAME = "test_image"
# working_dir = os.getcwd()

# file = open(FILE_NAME, "rb")

# # run_dir, work_dir = os.getcwd();
# my = file.read(1024)
# file.close()

# DIR = os.getcwd()

# # len(file)

# print(my)
# #print (file.read())

