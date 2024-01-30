#!/bin/sh

# Get the host's IP address by resolving the container's hostname
HOST_IP=$(getent hosts host.docker.internal | awk '{ print $1 }')

# export the host's IP address so pytest can use it
export HOST_IP

# Print information about the host's IP address
echo "Host IP Address: $HOST_IP"

# Run pytest with the host's IP address as an argument
pytest /tests
