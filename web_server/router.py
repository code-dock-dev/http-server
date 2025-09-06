import os
import logging

class Router:
    """
    Determines which file to serve based on the requested URL path.
    Implements basic routing, handles 404 Not Found errors, and includes
    basic security against path traversal attacks.
    """
    
    def __init__(self, public_dir='public'):
        self.public_dir = public_dir
    
    def _is_valid_file(self, file_path, public_dir_abs):
        """
        Checks if the requested file is within the public directory and
        is a valid file.
        """

        file_path_abs = os.path.abspath(file_path)
        return file_path_abs.startswith(public_dir_abs) and os.path.exists(file_path_abs) and os.path.isfile(file_path_abs)
    
    def get_route(self, path):
        """
        Translates a URL path to a local file path and determines the
        HTTP status code.
        
        Returns:
            A tuple of (file_path, status_code).
        """
        
        if path in ['/404', '/404.html']:
            return '/', 302
        
        if path == '/':
            path = '/index.html'

        public_dir_abs = os.path.abspath(self.public_dir)

        safe_path = os.path.abspath(os.path.normpath(os.path.join(self.public_dir, path.lstrip('/'))))
        if self._is_valid_file(safe_path, public_dir_abs):
            return safe_path, 200

        if not os.path.splitext(path)[1]:
            alt_path = os.path.abspath(os.path.normpath(os.path.join(self.public_dir, path.lstrip('/') + '.html')))
            if self._is_valid_file(alt_path, public_dir_abs):
                return alt_path, 200

        if not safe_path.startswith(public_dir_abs):
            logging.warning(f"Security Alert: Path traversal attempt blocked for '{path}'")
            return os.path.join(self.public_dir, '404.html'), 404

        logging.info(f"File not found for path: {path}. Serving 404 page.")
        return os.path.join(self.public_dir, '404.html'), 404