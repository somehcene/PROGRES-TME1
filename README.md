# PROGRES-TME1
Ma solution pour le premier TME du module Programmation Réseaux à sorbonne université 

## EXERCICE 1 Client/Server UDP
### Server (ServerUDP exo1.py)
* The server listens on port 1234 for incoming UDP messages.
*When a message is received from a client, it responds with a confirmation.
*The server has a random chance (50%) of not responding, simulating the unreliable nature of UDP.
### Client (clientUDP exo1.py)
*The client sends a message to the server and waits for a response.
*If no response is received, the client retries with an increased timeout.
*Once the client receives a response, it calculates the RTT (Round-Trip Time).
*The client allows multiple requests and calculates the average RTT.
***Why No Threading?***
Threading is not needed for this UDP server because:

*UDP is connectionless, meaning it does not maintain a dedicated connection to each client.
*The server can handle multiple requests from different clients naturally, without blocking, since each message is independent.
***Notes***
1. UDP does not guarantee message delivery, so some requests may be dropped randomly by design.
2. This project is a simple demonstration of UDP communication in Python.

## EXERCICE 2 Client/Server TCP 
This exercice contains a Python TCP client-server application where the client sends multiple requests for the server's current time. The server responds with the current time, and the client calculates the time difference for each request.

### Server (ServerHorloge exo2.py)
*The server listens for incoming TCP connections on port 1236.
*Once a client connects, it handles multiple requests from the client.
*The server sends the current time to the client in response to a specific request ("what time is it?").
*Each client is handled in a separate thread to allow multiple clients to connect simultaneously.

### Client (ClientHorloge exo2.py)
*The client connects to the server via TCP and requests the server's current time.
*The number of requests can be specified by the user.
*After sending each request, the client calculates and prints the time difference between when the request was sent and the server’s response time.

***Notes***
The server can handle multiple client requests simultaneously using threading.

## EXERCICE 3 HTTP Server 
This exercice contains a Python-based HTTP server that listens for client connections (such as web browsers) and serves an HTML response. This is a minimal HTTP server implementation built using Python's socket library. 
### HTTP Server (HTTPserver.py)
*The server listens on port 12345 for incoming HTTP requests.
*When a client (e.g., a web browser) sends a request, the server responds with a simple HTML page if the request is an HTTP GET request.
*If any errors occur during request handling, the server responds with a "500 Internal Server Error" message.
*Each client connection is handled in a separate thread, allowing for multiple clients to connect simultaneously.

***Access the Server from a Web Browser:***
1. Open a web browser.
2. Navigate to http://localhost:12345. 
3. You should see a simple HTML page that says "The web server is working."


