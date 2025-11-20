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
    time.sleep(0.5) # Give the port some time to initialize
    return tty_port, ups_data

def read_serial_data_EP20(ups_data, tty_port):
    try:
       print("read_serial_data_EP20()")
       if tty_port.isOpen():
           #byte_list0 = [0x0A, 0x03, 0x79, 0x18, 0x00, 0x07, 0x9c, 0x28] # handshake?
           byte_list1 = [0x0A, 0x03, 0x75, 0x30, 0x00, 0x1B, 0x1E, 0xB9] # responce 59 byte
           #byte_list2 = [0x0A, 0x03, 0x79, 0x18, 0x00, 0x0A, 0x5D, 0xED] # responce 25 byte

           ser.write(serial.to_bytes(byte_list1))
           print(f"Sent byte list: {byte_list1}")
           time.sleep(0.1) #0.1 is good value

           # Read binary data
           data1 = tty_port.read(59) # Read up to 59 bytes

           if data1:
               data1_size = sys.getsizeof(data1)
               print(f"Received data: {data1.hex()}") # Print as hex string
               print(f"Data size: {data1_size}") # Print as hex string
           else:
               print("No data received.")
    except:
        print("exception:something went wrong")
    finally:
        print("finally: end of read/write")


# MQTT Publisher
def publish_message(ups_data, time_interval):
    client = mqtt.Client()
    client.connect("localhost", 1883, 60)
    client.loop_start()
    _count = 0;
    while True:
#        message = f"Message {_count}"
        read_serial_data_EP20(ups_data, tty_port)
        message = f"Message #{_count}: {ups_data}"
        client.publish("test/topic", message)
        print(f"Published: {message}")
        _count += 1
        time.sleep(time_interval)
    client.loop_stop()
    client.disconnect()

if __name__ == "__main__":
    time_interval = 2; #sec, for debugging
    tty_port, ups_data = init_all('/dev/ttyUSB0');
    print (tty_port, ups_data);
    publish_message(ups_data, time_interval)
