import socket
import logging

from web_server.request_handler import RequestHandler

class Server:
    """
    A class to represent the core web server, responsible for managing the
    main socket and accepting new client connections.
    """

    def __init__(self):
        self.host = None
        self.port = None
        self.server_socket = None

    def run(self, host='0.0.0.0', port=8080):
        """
        Sets up the socket and enters the main loop to listen for and
        handle incoming connections.
        """
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()
        
        logging.info(f"Server is listening on http://{self.host}:{self.port}")
        logging.info("Press Ctrl+C to stop the server.")

        while True:
            try:
                client_socket, client_address = self.server_socket.accept()
                logging.info(f"Accepted connection from {client_address}")
                
                handler = RequestHandler(client_socket)
                handler.handle_request()
                
            except KeyboardInterrupt:
                logging.info("Server shutting down.")
                break
            except Exception as e:
                logging.error(f"An error occurred in the server loop: {e}", exc_info=True)
                continue
        
        if self.server_socket:
            self.server_socket.close()

