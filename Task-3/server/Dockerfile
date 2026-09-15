FROM python:3.11-slim

WORKDIR /app

# Copy the server script
COPY server.py .

# Expose port 5000
EXPOSE 5000

# Start the python server
CMD ["python", "-u", "server.py"]
