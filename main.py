import socket

HOST = '0.0.0.0'  # Standard loopback interface address (localhost)
PORT = 8080      # Port to listen on (non-privileged ports are > 1023)

def handle_request(client_socket):
    """
    Handles a single client request by reading the data, constructing a response,
    and sending it back.
    """
    # Receive data from the client
    request_data = client_socket.recv(1024).decode('utf-8')
    
    # Print the received request to the console for debugging
    print("Received Request:")
    print(request_data)

    # Simple logic to determine the response
    # This server only handles a single static page response.
    # In a real-world server, you would parse the request headers and path
    # to determine what content to serve.

    # Start with the HTTP status line
    response_line = "HTTP/1.1 200 OK\r\n"
    
    # Add headers
    content_type_header = "Content-Type: text/html\r\n"
    connection_header = "Connection: close\r\n" # This tells the client to close the connection after the response
    
    # Add a blank line to separate headers from content
    blank_line = "\r\n"

    # Define the HTML content to be served
    response_content = "<html><body><h1>Hello from my Python server!</h1><p>This is a super simple HTTP server built from scratch.</p></body></html>"

    # Combine all parts to form the full HTTP response
    full_response = (response_line + 
                     content_type_header + 
                     connection_header +
                     blank_line +
                     response_content)
    
    # Encode the string into bytes and send it back to the client
    client_socket.sendall(full_response.encode('utf-8'))

def run_server():
    """
    Sets up and runs the server loop to listen for incoming connections.
    """
    # Create a socket object using the AF_INET address family (for IPv4)
    # and the SOCK_STREAM socket type (for TCP)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # The `bind()` method binds the socket to the specified address and port
        server_socket.bind((HOST, PORT))
        
        # The `listen()` method enables a server to accept connections
        # The argument specifies the number of unaccepted connections that the system will allow
        server_socket.listen()
        
        print(f"Server is listening on http://{HOST}:{PORT}")
        print("Press Ctrl+C to stop the server.")

        # The main server loop
        while True:
            try:
                # The `accept()` method waits for an incoming connection and returns a new socket
                # representing the connection, and the address of the client
                client_socket, client_address = server_socket.accept()
                
                print(f"Accepted connection from {client_address}")
                
                # Handle the request in a separate function
                handle_request(client_socket)
                
                # The `with` statement ensures the socket is properly closed after use
            except KeyboardInterrupt:
                print("\nServer shutting down.")
                break
            except Exception as e:
                print(f"An error occurred: {e}")
                # Continue the loop even if an error occurs with one client

if __name__ == "__main__":
    run_server()
