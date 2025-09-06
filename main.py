import logging
import socket

HOST = '0.0.0.0'
PORT = 8080

def handle_request(client_socket):
    """
    Handles a single client request by reading data, constructing a response,
    and sending it back, with robust error handling.
    """
    with client_socket:
        try:
            request_data_bytes = client_socket.recv(1024)
            if not request_data_bytes:
                logging.warning("Client disconnected.")
                return

            request_data = request_data_bytes.decode('utf-8')
            request_line = request_data.splitlines()[0] if request_data else ''
            logging.info(request_line)

            response_line = "HTTP/1.1 200 OK\r\n"
            content_type_header = "Content-Type: text/html\r\n"
            connection_header = "Connection: close\r\n"
            blank_line = "\r\n"
            response_content = "<html><body><h1>Hello, Browser!</h1></body></html>"
            
            full_response = (response_line + 
                             content_type_header + 
                             connection_header +
                             blank_line +
                             response_content)
            
            client_socket.sendall(full_response.encode('utf-8'))

        except (BrokenPipeError, ConnectionResetError, socket.error) as e:
            logging.error(f"Socket error while handling request: {e}")

def run_server():
    """
    Sets up and runs the server loop to listen for incoming connections.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        
        logging.info(f"Server is listening on http://{HOST}:{PORT}")
        logging.info("Press Ctrl+C to stop the server.")

        while True:
            try:
                client_socket, client_address = server_socket.accept()
                logging.info(f"Accepted connection from {client_address}")
                handle_request(client_socket)
                
            except KeyboardInterrupt:
                logging.info("\nServer shutting down.")
                break
            except Exception as e:
                logging.error(f"An error occurred: {e}")
                continue

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    run_server()
