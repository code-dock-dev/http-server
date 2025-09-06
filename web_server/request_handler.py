import logging
from socket import error as socket_error

from web_server.response_builder import ResponseBuilder
from web_server.router import Router

class RequestHandler:
    """
    Handles a single client connection, from parsing the request to
    sending the final response.
    """

    def __init__(self, client_socket):
        self.client_socket = client_socket
        self.router = Router()
        self.response_builder = ResponseBuilder()
    
    def handle_request(self):
        """
        Manages the full lifecycle of a single request.
        """

        with self.client_socket:
            try:
                request_data_bytes = self.client_socket.recv(1024)
                
                if not request_data_bytes:
                    logging.info("Client disconnected.")
                    return

                request_data = request_data_bytes.decode('utf-8')
                first_line = request_data.split('\r\n')[0]
                logging.info(first_line)
                
                parts = first_line.split(' ')
                if len(parts) > 1:
                    path = parts[1]
                else:
                    path = "/"

                file_path, status_code = self.router.get_route(path)
                response = self.response_builder.build_response(file_path, status_code)
                self.client_socket.sendall(response)
                logging.info(f"Response sent for {path} with status {status_code}.")

            except (BrokenPipeError, ConnectionResetError, socket_error) as e:
                logging.warning(f"Socket error while handling request: {e}")