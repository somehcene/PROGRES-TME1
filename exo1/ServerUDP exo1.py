import numpy
import random 

from socket import *
    

def run_server():
    """
    Function that runs a server UDP socket and waits for clients to send requests """
    serverPort = 1234
    serverSocket = socket(AF_INET,SOCK_DGRAM) 
    serverSocket.bind(("",serverPort))
    print("server ready\n")
    while True:
        _, client_ip = serverSocket.recvfrom(2048)
        print(f"Message recieved from client '{client_ip}'")
        if random.random() > 0.5:
            print("Oops, i forgot to respond\n")
            continue
        serverSocket.sendto("message from server to client".encode('utf-8'), client_ip)
        print(f"Message sent to client '{client_ip}'")
      
    
    
if __name__ == '__main__':
    run_server()

