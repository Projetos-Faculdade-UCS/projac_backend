#!/bin/bash

# Default Dockerfile and image tag
DOCKERFILE="Dockerfile"
IMAGE_TAG="projac:0.1"

# Parse command-line arguments
while [[ "$#" -gt 0 ]]; do
    case $1 in
        --prod) DOCKERFILE="Dockerfile.prod"; IMAGE_TAG="projac:0.1-prod"; shift ;;
        *) echo "Unknown parameter passed: $1"; exit 1 ;;
    esac
    shift
done

# Build the Docker image with the specified Dockerfile and image tag
docker build -t $IMAGE_TAG -f $DOCKERFILE .

echo "Docker image built using $DOCKERFILE with tag $IMAGE_TAG"
