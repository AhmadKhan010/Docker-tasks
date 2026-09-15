FROM python:3.11-slim

WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the client script
COPY client.py .

# Use python -u to run unbuffered, so logs appear immediately in Docker
CMD ["python", "-u", "client.py"]
