import socket
import os
ipAddr = "127.0.0.1"
port = 12345
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketAddr = (ipAddr, port)
#bind the port
sk.bind(socketAddr)
try:
    sk.listen(1)
except socket.error:
    print("fail to connect")

while True:
    print("Waiting for connection")
    client, addr = sk.accept()
    print("A connection has been accepted")
    client.close()
