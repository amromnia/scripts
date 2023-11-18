import socket
import random
import datetime
# Create a socket object
import time

# send a message to server

def send_msg(server):
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")

    msg = {
        "type": "trade",
        "from_meter": 1,
        "to_meter": 2,
    }
    server.send(bytes(str(msg), 'utf-8'))

def main():
    port = 1235
    # send msg with 1 second interval
    # while True:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect(('localhost', port))
    send_msg(server)
    server.close()
    time.sleep(1)


if __name__ == "__main__":
    main()