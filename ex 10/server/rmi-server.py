import Pyro4
import random
import os

@Pyro4.expose
class Kerberos(object):
    def get_fortune(self, name):
        return "Hello, {0}. Here is your fortune message:\n" \
               "Tomorrow's lucky number is {1}.".format(name, random.randint(0,1000))
               
    def add(self, a, b):
        return "{0} + {1} = {2}".format(a, b, int(a)+int(b))
    
    def substract(self, a, b):
        return "{0} - {1} = {2}".format(a, b, int(a)-int(b))
    
    def multiply(self, a, b):
        return "{0} - {1} = {2}".format(a, b, int(a)*int(b))
    
    def divide(self, a, b):
        return "{0} - {1} = {2}".format(a, b, int(a)/int(b))
    


daemon = Pyro4.Daemon()                # make a Pyro daemon
ns = Pyro4.locateNS()                  # find the name server
uri = daemon.register(Kerberos)   # register the greeting maker as a Pyro object
ns.register("example.kerb", uri)   # register the object with a name in the name server

print("Hi. Kerberos is now active.")
daemon.requestLoop()                   # start the event loop of the server to wait for calls