# PROGRES-TME1
Ma solution pour le premier TME du module Programmation Réseaux à sorbonne université 

# EXERCICE 1 Client/Serveur UDP
How It Works?
# Server (ServerUDP exo1.py)
The server listens on port 1234 for incoming UDP messages.
When a message is received from a client, it responds with a confirmation.
The server has a random chance (50%) of not responding, simulating the unreliable nature of UDP.
# Client (clientUDP exo1.py)
The client sends a message to the server and waits for a response.
If no response is received, the client retries with an increased timeout.
Once the client receives a response, it calculates the RTT (Round-Trip Time).
The client allows multiple requests and calculates the average RTT.
Why No Threading?
Threading is not needed for this UDP server because:

UDP is connectionless, meaning it does not maintain a dedicated connection to each client.
The server can handle multiple requests from different clients naturally, without blocking, since each message is independent.
