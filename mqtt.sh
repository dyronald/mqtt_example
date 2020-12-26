#!/bin/bash

POD=littlestmq

down() {
    podman pod stop $POD
    podman pod rm $POD
}

if [ $1 == "restart" ]
then
    down

    podman pod create \
        --name=$POD \
        --publish "1883:1883"

    podman run -dt --pod=$POD \
        --name=$POD-mqtt-server \
        $POD-mqtt-server

elif [ $1 == "down" ]
then
    down

elif [ $1 == "build" ] 
then
    pushd .
    cd mqtt_server
    podman build -t $POD-mqtt-server .
    popd

fi