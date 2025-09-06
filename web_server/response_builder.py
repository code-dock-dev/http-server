class ResponseBuilder:
    """
    A generic component for constructing valid HTTP responses.
    """
    def build_response(self, file_path, status_code):
        """
        Builds a full HTTP response with appropriate headers and content.
        
        Args:
            file_path (str): The path to the file to be served.
            status_code (int): The HTTP status code (e.g., 200 or 404).
            
        Returns:
            The full HTTP response as bytes.
        """
        status_messages = {
            200: "OK",
            404: "Not Found",
            302: "Found"
        }
        status_text = status_messages.get(status_code, "OK")

        if status_code == 302:
            # Redirect response
            response_line = f"HTTP/1.1 302 Found\r\n"
            location_header = "Location: /\r\n"
            connection_header = "Connection: close\r\n"
            blank_line = "\r\n"
            content = "<h1>Redirecting to /</h1>"
            content_type_header = "Content-Type: text/html; charset=utf-8\r\n"
            content_length = len(content.encode('utf-8'))
            content_length_header = f"Content-Length: {content_length}\r\n"
            full_response = (response_line +
                             location_header +
                             content_type_header +
                             content_length_header +
                             connection_header +
                             blank_line +
                             content)
            return full_response.encode('utf-8')

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except FileNotFoundError:
            content = "<h1>500 Internal Server Error: Critical file missing</h1>"
            status_code = 500
            status_text = "Internal Server Error"

        response_line = f"HTTP/1.1 {status_code} {status_text}\r\n"
        content_type_header = "Content-Type: text/html; charset=utf-8\r\n"
        content_length = len(content.encode('utf-8'))
        content_length_header = f"Content-Length: {content_length}\r\n"
        connection_header = "Connection: close\r\n"
        blank_line = "\r\n"

        full_response = (response_line +
                         content_type_header +
                         content_length_header +
                         connection_header +
                         blank_line +
                         content)
        return full_response.encode('utf-8')