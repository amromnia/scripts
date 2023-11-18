import socket
import random
import datetime
# Create a socket object
import time

# send a message to server

def send_msg(server):
    now = datetime.datetime.now() - datetime.timedelta(hours=10)
    current_time = now.strftime("%H:%M:%S")




    msg = {
        "type": "update",
        "time": current_time,
        "meter_update":
            [
                {
                    "generation": random.randint(0, 1000),
                    "consumption": random.randint(0, 1000),
                },
                {
                    "generation": random.randint(0, 1000),
                    "consumption": random.randint(0, 1000),
                },
                {
                    "generation": random.randint(0, 1000),
                    "consumption": random.randint(0, 1000),
                },{
                    "generation": random.randint(0, 1000),
                    "consumption": random.randint(0, 1000),
                },
                {
                    "generation": random.randint(0, 1000),
                    "consumption": random.randint(0, 1000),
                },
                {
                    "generation": random.randint(0, 1000),
                    "consumption": random.randint(0, 1000),
                },{
                    "generation": random.randint(0, 1000),
                    "consumption": random.randint(0, 1000),
                },
                {
                    "generation": random.randint(0, 1000),
                    "consumption": random.randint(0, 1000),
                },
                {
                    "generation": random.randint(0, 1000),
                    "consumption": random.randint(0, 1000),
                },{
                    "generation": random.randint(0, 1000),
                    "consumption": random.randint(0, 1000),
                },
                {
                    "generation": random.randint(0, 1000),
                    "consumption": random.randint(0, 1000),
                },
                {
                    "generation": random.randint(0, 1000),
                    "consumption": random.randint(0, 1000),
                }
            ]
    }
    server.send(bytes(str(msg), 'utf-8'))

def main():
    port = 1234
    # send msg with 1 second interval
    while True:
        try:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.connect(('localhost', port))
            send_msg(server)
            server.close()
            time.sleep(1)
        except:
            pass


if __name__ == "__main__":
    main()