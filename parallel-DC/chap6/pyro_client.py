import Pyro4

name = input("What is your name? ").strip()

server = Pyro4.Proxy("PYRONAME:server")
print(server.welcomeMessage(name))
