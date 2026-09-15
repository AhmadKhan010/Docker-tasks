# Rakurai Training: Docker Tasks

This repository contains the completion of Docker-related tasks as part of the Training at Rakurai. The tasks cover Docker installation, basic commands, creating custom Docker images, and setting up multi-container applications using Docker Compose.

## Task 1: Installation and Basic Usage
*Note: There are no files associated with this task in the repository, as it focused on local installation and executing basic commands.*

**Description**: 
This task involved installing Docker and validating its installation using the standard `hello-world` image. Additionally, it involved interacting with the official NGINX Docker image.

**How it was completed**:
1. Installed Docker on the local machine and verified the installation by running:
   ```bash
   docker run hello-world
   ```
2. Pulled and ran the official `nginx` Docker image in detached mode:
   ```bash
   docker run -d -p 8080:80 --name my-nginx nginx
   ```
3. Accessed the web server locally via the browser at `http://localhost:8080`.
4. Stopped and removed the container:
   ```bash
   docker stop my-nginx
   docker rm my-nginx
   ```

---

## Task 2: Building and Running a Custom Docker Image
**Directory**: `Task-2`

**Description**: 
This task focused on creating a custom Docker image equipped with essential development tools like CMake, Make, Python, Git, and GCC. It also demonstrated compiling and running a C++ application within the container and utilizing volume mapping as a non-root user.

**How it was completed**:
1. Created a `Dockerfile` that installs the required dependencies (CMake, Make, Python3, Git, GCC).
2. Set up a non-root user within the container to ensure secure volume mapping with the host.
3. Created a simple C++ application in the `src` folder.

**How to run**:
1. Navigate to the `Task-2` directory.
2. Build the Docker image:
   ```bash
   docker build -t my-cpp-env .
   ```
3. Run the container with volume mapping (mapping the local `src` folder to the container):
   ```bash
   docker run -it -v $(pwd)/src:/app/src my-cpp-env
   ```
4. Inside the container, build and run the C++ application using `g++` or `cmake`.
5. Finally, the image was pushed to Docker Hub using `docker push`.

---

## Task 3: Docker Compose (Python Server-Client)
**Directory**: `Task-3`

**Description**:
This task introduced `docker-compose` to orchestrate a multi-container environment. It consists of a Python server and a Python client communicating over a private Docker network. 

The server provides:
- `GET /health` - Health check endpoint.
- `POST /ping` - Returns a pong with the current time.
- `POST /data` - Accepts a JSON-RPC message and responds with the original message plus a timestamp.

The client sends a sequence of these requests repeatedly every 5 seconds.

**How it was completed**:
1. Developed the Python server (`server/`) and Python client (`client/`) scripts.
2. Written a `docker-compose.yml` defining the two services.
3. Configured `depends_on` with `condition: service_healthy` so that the client waits for the server's health check to pass before starting.

**How to run**:
1. Navigate to the `Task-3` directory.
2. Start the services using Docker Compose:
   ```bash
   docker-compose up --build
   ```
3. Observe the client and server logs in the terminal as the client makes API requests every 5 seconds.
4. To stop the application, use `Ctrl+C` or run:
   ```bash
   docker-compose down
   ```
