import serial
import struct
import time
import sys

import paho.mqtt.client as mqtt

#ser = serial.Serial(
#    port='/dev/ttyUSB0',
#    baudrate=9600,
#    bytesize=serial.EIGHTBITS,
#    parity=serial.PARITY_NONE,
#    timeout=1 # Read timeout in seconds
#)


def init_all(port_name):
    print("init_all()")
    data0 = b"00000000000000000000000000000000000000000000000000000000000"
    format_string = '>BHHHHHHHHHHHHHHHHHHHHHHHHHHHI'
    ups_data = struct.unpack(format_string, data0)

    tty_port = serial.Serial(
#        port='/dev/ttyUSB0',
        port=port_name,
        baudrate=9600,
        bytesize=serial.EIGHTBITS,
        parity=serial.PARITY_NONE,
        timeout=1 # Read timeout in seconds
    )

    return ups_data, tty_port

def read_serial_data_EP20():
    try:
       print("read_serial_data_EP20()")
    except:
        print("exception:something went wrong")
    finally:
        print("finally: bye-bye")


# MQTT Publisher
def publish_message(ups_data):
    client = mqtt.Client()
    client.connect("localhost", 1883, 60)
    client.loop_start()
    _count = 0;
    while True:
#        message = f"Message {_count}"
        message = f"Message #{_count}: {ups_data}"
        client.publish("test/topic", message)
        print(f"Published: {message}")
        _count += 1
        time.sleep(1)
    client.loop_stop()
    client.disconnect()

if __name__ == "__main__":
    ups_data, tty_port = init_all('/dev/ttyUSB0');
    print (ups_data, tty_port);
    read_serial_data_EP20()
    publish_message(ups_data)
