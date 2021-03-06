import socket
from threading import Thread

IP_ADDRESS = '127.0.0.1'
PORT = 8050
SERVER = None
BUFFER_SIZE = 4096
clients = {}

def acceptConnections():
    global SERVER
    global clients

    while True:
        client, addr = SERVER.accept()
        print(client.addr)

def setup():
    print("\n\t\t\t\t\t\t\t\t IP MESSENGER\n")

    # getting global variables 
    global PORT
    global IP_ADDRESS
    global SERVER

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))
    
    # Listening to incoming connections
    SERVER.listen(100)

    print("\t\t\t\tServer Is Waiting for Incoming Connections...")
    print("\n")


    acceptConnections()

setup_thread = Thread(target=setup)
setup_thread.start()
