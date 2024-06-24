#!/bin/bash

# Default image tag
IMAGE_TAG="projac:0.1"

# Parse command-line arguments
while [[ "$#" -gt 0 ]]; do
    case $1 in
        --prod) IMAGE_TAG="projac:0.1-prod"; shift ;;
        *) echo "Unknown parameter passed: $1"; exit 1 ;;
    esac
    shift
done

# Run the Docker container with the specified image tag
docker run -it -p 8000:8000 -v ./app:/app $IMAGE_TAG /bin/bash

echo "Docker container running using image $IMAGE_TAG"
