import json
import logging
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
from datetime import datetime

# Configure logging to write to both a file and standard output (console)
logger = logging.getLogger("server_logger")
logger.setLevel(logging.INFO)

# Create handlers
stream_handler = logging.StreamHandler(sys.stdout)
file_handler = logging.FileHandler("server.log")

# Create formatters and add it to handlers
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%H:%M:%S')
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(stream_handler)
logger.addHandler(file_handler)

class SimpleHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        # Override default logging to use our custom logger
        logger.info("%s - %s" % (self.address_string(), format%args))

    def get_current_time(self):
        return datetime.now().isoformat()

    def do_GET(self):
        logger.info(f"Received GET request on {self.path}")
        if self.path == '/health':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        logger.info(f"Received POST request on {self.path}")
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)

        try:
            data = json.loads(post_data.decode('utf-8'))
        except json.JSONDecodeError:
            logger.error("Failed to parse JSON data")
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Invalid JSON")
            return

        if self.path == '/ping':
            if data.get('type') == 'ping':
                response = {
                    "type": "pong",
                    "time": self.get_current_time()
                }
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(response).encode('utf-8'))
            else:
                logger.warning("Invalid ping request data")
                self.send_response(400)
                self.end_headers()

        elif self.path == '/data':
            if data:
                data['time'] = self.get_current_time()
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(data).encode('utf-8'))
            else:
                logger.warning("Empty data request")
                self.send_response(400)
                self.end_headers()
        else:
            logger.warning(f"Endpoint not found: {self.path}")
            self.send_response(404)
            self.end_headers()

if __name__ == '__main__':
    server_address = ('', 5000)
    httpd = HTTPServer(server_address, SimpleHandler)
    logger.info("Starting simple python server on port 5000...")
    httpd.serve_forever()
