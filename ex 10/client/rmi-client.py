# saved as client.py
import Pyro4
kerberos = Pyro4.Proxy("PYRONAME:example.kerb")    # use name server object lookup uri shortcut

name = input("What is your name? ").strip()
print(kerberos.get_fortune(name))

a,b = input("Enter 'a', 'b' for addition: ").split(' ')
print(kerberos.add(a,b))

a,b = input("Enter 'a', 'b' for multiplication: ").split(' ')
print(kerberos.multiply(a,b))

a,b = input("Enter 'a', 'b' for division: ").split(' ')
print(kerberos.divide(a,b))

a,b = input("Enter 'a', 'b' for substraction: ").split(' ')
print(kerberos.substract(a,b))