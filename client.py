from socket_client import SocketClient

socket_client = SocketClient(socket_numbers=2)
socket_client.add_socket({
    "host": "192.168.1.163",
    "port": 12345
}).add_socket({
    "host": "192.168.1.211",
    "port": 12345
})
socket_client.start()
