#!/bin/sh

# if ! docker network ls | tail -n +2 | awk '{ print $2 }' | grep mongo-net > /dev/null; then
#     echo "Creating network"
#     docker network create --driver bridge mongo-net
# fi
# --network mongo-net \
docker run -d --rm \
    --name mongod \
    -p 27042:27017 \
    -e MONGO_INITDB_ROOT_USERNAME=mongoadmin \
    -e MONGO_INITDB_ROOT_PASSWORD=abacab \
    mongo
