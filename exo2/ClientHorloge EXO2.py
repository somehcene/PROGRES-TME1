import socket
import datetime
import random
import time

BUFFER_SIZE = 2048


def run_client(server_ip='localhost', server_port=1236 , request_count=int(input("what's the request count : "))):
    """
    Function that runs a client, connects to the server and send requests for current server time 
    """
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))
    
    print(f"Connected to server {server_ip}:{server_port}")
    
    # Sending request number to the server 
    client_socket.send(request_count.to_bytes(4, byteorder='big'))
    
    time_differences = []
    
    for i in range(request_count):
        time.sleep(random.uniform(0.5, 2))  # This is a way to kind of simulate a realistic situation 
        
        # Send request 
        time_sent = datetime.datetime.now().isoformat()
        client_socket.send("what tume is it ?".encode('utf-8'))
        
        # Recieving server's time
        time_received = client_socket.recv(BUFFER_SIZE).decode('utf-8')
        
        # Compute the time difference
        time_difference = datetime.datetime.fromisoformat(time_received) - datetime.datetime.fromisoformat(time_sent) 
        time_differences.append(time_difference)
        
        print(f"Request number {i+1}: sent at {time_sent}, recieved at {time_received}")
        print(f"Time difference: {time_difference}")
    
    client_socket.close()
    return time_differences

if __name__ == '__main__':
    run_client()
