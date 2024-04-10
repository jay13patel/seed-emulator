# Use Python 3.7 slim as base image
FROM python:3.7-slim

# Set default environment variables for WebSocket and CARLA servers
ENV WS_IP="127.0.0.1" \
    WS_PORT=6789 \
    CARLA_IP="127.0.0.1" \
    CARLA_PORT=2000

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run webserver.py when the container launches
CMD ["sh", "-c", "python webserver.py --ws_ip=${WS_IP} --ws_port=${WS_PORT} --carla_ip=${CARLA_IP} --carla_port=${CARLA_PORT}"]