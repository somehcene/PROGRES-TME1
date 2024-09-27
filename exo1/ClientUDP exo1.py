import socket
import time
import numpy as np

def run_client():
    """
    Function that run a client UDPsocket that requests the the server's current time 
    it takes no parameters"""
    server_ip = 'localhost'
    server_port = 1234 
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print(f"Sending message to server ...")
    start = time.time()
    delay = 0.1
    while True:
        client_socket.sendto("Sending message from client to server".encode('utf-8'), (server_ip, server_port))
        client_socket.settimeout(delay)
        try:
            _, server_ip = client_socket.recvfrom(2024)
        except socket.timeout:
            delay *= 2
        else:
            break
    done = time.time()
    print(f"'{server_ip}.{server_port} recieved the message and responded "
          f"with a timespan of = {done-start} seconds")

    client_socket.close() 

    return done - start 

import numpy as np  # For calculating the mean of RTTs

if __name__ == '__main__':
    n = 0  # Counter for the number of messages sent
    rtt_values = [] 

    while True:
        try:
            user_input = int(input("Type 1 to keep requesting server's time and 0 to stop the program: "))
            
            if user_input == 0:  # If the user types 0, exit the loop
                break
            elif user_input == 1:  # If the user types 1, continue
                rtt = run_client()  # Call the function to send a request and get the RTT
                rtt_values.append(rtt) 
                n += 1 
            else:
                print("Please enter 0 or 1 only.")
        
        except ValueError:
            print("Invalid input. Please enter an integer (0 or 1).")

    print(f"\nMessages sent = {n}")
    if rtt_values:
        print(f"\nRTT mean = {np.mean(rtt_values):.6f} seconds")  # Calculate and display the mean RTT
    else:
        print("No messages were sent.")
