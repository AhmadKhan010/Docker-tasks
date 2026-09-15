import requests
import time
import logging
import sys
from datetime import datetime

# Configure logging to write to both a file and standard output (console)
logger = logging.getLogger("client_logger")
logger.setLevel(logging.INFO)

# Create handlers
stream_handler = logging.StreamHandler(sys.stdout)
file_handler = logging.FileHandler("client.log")

# Create formatters and add it to handlers
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%H:%M:%S')
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(stream_handler)
logger.addHandler(file_handler)


# The server is accessible via its docker-compose service name "server"
SERVER_URL = "http://server:5000"

def run_client():
    logger.info("Starting Python client loop...")
    
    while True:
        try:
            # 1. Perform Health Check
            logger.info("Sending GET request to /health")
            health_res = requests.get(f"{SERVER_URL}/health")
            logger.info(f"Health Check Response: {health_res.text} (Status: {health_res.status_code})")

            # 2. Send Ping Request
            logger.info("Sending POST request to /ping")
            ping_data = {"type": "ping"}
            ping_res = requests.post(f"{SERVER_URL}/ping", json=ping_data)
            logger.info(f"Ping Response: {ping_res.json()}")

            # 3. Send Data Request
            logger.info("Sending POST request to /data")
            data_req = {"jsonrpc": "2.0", "method": "message-1"}
            data_res = requests.post(f"{SERVER_URL}/data", json=data_req)
            logger.info(f"Data Response: {data_res.json()}")
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Connection failed: {e}")
            
        logger.info("Waiting 5 seconds before the next request cycle...\n")
        time.sleep(5)

if __name__ == "__main__":
    # Start the continuous loop
    run_client()
