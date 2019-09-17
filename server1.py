from server_copy import ServerCopy

socket_server = ServerCopy()
socket_server.config({
    "host": "192.168.1.163",
    "port": 12345
}).start()
