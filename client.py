import socket
import os
import requests
ipAddr = "127.0.0.1"
port = 12345
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    socketAddr = (ipAddr, port)
    sk.connect(socketAddr)
    print("IP " + ipAddr + "#" + str(port)  + " connection is successful!")
except socket.error:
    print("Fail to build connection")
    sk.close()