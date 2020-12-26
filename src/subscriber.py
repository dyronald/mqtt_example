import paho.mqtt.client as mqtt


broker_address = 'localhost'
client_name = 'Sub1'
topic = 'T1'


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

def on_subscribe(client, userdata, mid, granted_qos):
    print('subsribed')

def on_message(client, userdata, message):
    print(f'{userdata}: {message.payload}')


if __name__ == '__main__':
    client = mqtt.Client(client_name)
    client.on_message = on_message
    client.on_subscribe = on_subscribe
    client.on_connect = on_connect

    client.connect(broker_address)

    client.loop_start()

    client.subscribe(topic)
    input('listening...')

    client.loop_stop()
    client.disconnect()
