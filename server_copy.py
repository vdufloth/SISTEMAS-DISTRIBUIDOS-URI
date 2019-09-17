import socket
import time
import random


class ServerCopy:

    def __init__(self):
        self.host = None
        self.port = None

    def config(self, server_config):
        self.host = server_config['host']
        self.port = server_config['port']
        return self

    def validate(self):
        if not self.host or not self.port:
            raise Exception("Host and port are required")

    def fat(self, n):
        t = 1
        for i in range(2, n+1):
            t *= i
        rand = random.randint(3, 7)
        time.sleep(rand)
        return t

    def start(self):
        self.validate()

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen()
            conn, addr = s.accept()
            with conn:
                while True:
                    try:
                        data = conn.recv(1024)
                        if data:
                            calc = self.fat(int(float(data)))
                            conn.send(str(calc).encode())
                    except Exception as ex:
                        print(ex)
