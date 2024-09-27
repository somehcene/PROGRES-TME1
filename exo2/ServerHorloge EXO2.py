import socket
import threading
import datetime




def handle_client(client_socket):
    """
    Handles communication with a spécific client takes the the socket as the only parameter
    """
    try:
        # Recieving the number of requests from a specfc client
        count_data = client_socket.recv(2048)
        if not count_data:
            client_socket.close()
            return
        
        count = int.from_bytes(count_data, byteorder='big')
        
        for _ in range(count):
            # Recieving the request from a specific client
            client_message = client_socket.recv(2048).decode('utf-8')
            if client_message == "what tume is it ?":
                # Sending current server hour to client
                current_time = datetime.datetime.now().isoformat()
                client_socket.send(current_time.encode('utf-8'))
    finally:
        # Using finally unsures that, whatever happens on the try block, the server does not stay n a blocked state 
        client_socket.close()

def run_server(server_port=1236):
    """
    Runs server and listens to connection requests 
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', server_port))
    server_socket.listen(5)
    print(f"Server s ready for connection requests on port {server_port}...")

    while True:
        # Accept client's connexions 
        client_socket, client_address = server_socket.accept()
        print(f"Connexon request from client {client_address}")
        
        # Lancer un thread pour chaque client
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == '__main__':
    run_server()
