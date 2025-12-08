import argparse

parser = argparse.ArgumentParser(description='EP20 commnad-line parser')

parser.add_argument('--port', dest='port', type=str, default="/dev/ttyUSB0",
                    help='port to connect to MustPower EP20')

args = parser.parse_args()

print (f"port {args.port}")
