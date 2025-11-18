# pip install paho-mqtt
# Raspberry Pi installation https://randomnerdtutorials.com/how-to-install-mosquitto-broker-on-raspberry-pi/

# mosquitto_sub -d -t test/topic

import paho.mqtt.client as mqtt
import time

# Publisher
def publish_message():
    client = mqtt.Client()
    client.connect("127.0.0.1", 1883, 60)
    client.loop_start()
    _count = 0;
    while True:
#    for i in range(256):
        message = f"Message {_count}"
        client.publish("test/topic", message)
        print(f"Published: {message}")
        _count += 1
        time.sleep(1)
    client.loop_stop()
    client.disconnect()

# Subscriber
def subscribe_messages():
    def on_connect(client, userdata, flags, rc):
        print(f"Connected with result code {rc}")
        client.subscribe("test/topic")

    def on_message(client, userdata, msg):
        print(f"Received: Topic: {msg.topic}, Payload: {msg.payload.decode()}")

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("broker.emqx.io", 1883, 60)
    client.loop_forever() # Keep the client running to receive messages

print ("\n\tThis will run infinity loop on localhost and send test data to test/topic\n")
publish_message()
# subscribe_messages()
