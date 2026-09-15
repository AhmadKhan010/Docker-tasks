FROM ubuntu:22.04


# Install the requested tools: CMake, Make, Python3, Git, GCC, g++ and nano
RUN apt-get update && apt-get install -y cmake make python3 python-is-python3 git gcc g++ nano && rm -rf /var/lib/apt/lists/*


# Create a non-root user named 'devuser' with ID 1000
RUN groupadd -g 1000 devgroup && \
    useradd -u 1000 -g 1000 devuser

# Create directories and set ownership
RUN mkdir /app /workspace && chown devuser:devgroup /app /workspace

# Switch to the non-root user
USER devuser

# Build the C++ application inside the Dockerfile
# Copy the source code into the image 
COPY --chown=devuser:devgroup src/ /app/src/

# Compile the C++ application
WORKDIR /app
RUN g++ src/main.cpp -o my_cpp_app

# Set the default working directory for when the container runs
WORKDIR /workspace

# Run the pre-built application when the container starts, then open a shell
CMD ["sh", "-c", "/app/my_cpp_app && exec /bin/bash"]
