import paho.mqtt.client as mqtt
from coolname import generate
import time

broker_address = 'localhost'
client_name = 'Pub1'
topic = 'T1'

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

if __name__ == '__main__':
    client = mqtt.Client(client_name)
    client.on_connect = on_connect

    client.connect(broker_address, 1883, 60)

    message = '-'.join(generate())
    print(message)
    client.publish(topic=topic, payload=message)
    client.disconnect()
