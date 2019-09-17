import socket
from threading import Thread
import time


class SocketClient:

    def __init__(self, socket_numbers):
        self.SOCKET_NUMBERS = socket_numbers
        self.SOCKET_SERVERS = []
        self.RESPONSES = []

    def validate(self):
        pass

    def add_socket(self, socket):
        self.SOCKET_SERVERS.append(socket)
        return self

    def send_message(self, host, port, value, i):
        try:
            start = time.time()
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((host, port))
            sock.send(str(value).encode())
            result = sock.recv(1024)
            done = time.time()
            self.RESPONSES.append({
                "server_id": i,
                "send": str(value),
                "value": result,
                "duration": round(done - start, 2)
            })
            #sock.close()
        except Exception as ex:
            print("Servidor %d está inativo." % i)

    def start(self):
        self.validate()
        while True:
            n = int(input("Digite o valor para calcular o fatorial: "))
            thread_list = []

            for i in range(1, self.SOCKET_NUMBERS+1):
                current_socket = self.SOCKET_SERVERS[i-1]
                client_thread = Thread(target=self.send_message, args=(current_socket["host"], current_socket["port"], n, i))
                thread_list.append(client_thread)
                client_thread.start()

            [x.join() for x in thread_list]

            print(self.RESPONSES)
