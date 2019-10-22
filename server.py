import socket
import os
import requests
import datetime
import time
from wsgiref.handlers import format_date_time
ipAddr = "127.0.0.1"
port = 80
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketAddr = (ipAddr, port)
#bind the port
sk.bind(socketAddr)
try:
    sk.listen(1)
except socket.error:
    print("Fail to connect")

print("Waiting for connection")
client, addr = sk.accept()
#print("A connection has been accepted")
msg = client.recv(4096)
msg = msg.decode("utf-8")
header = msg.split("\r\n")
try:
    method = header[0].split(" ")[0]
    obj = header[0].split(" ")[1].replace("/", "\\")
except:
    print(header)
if method == "GET":
    path = "." + obj
    if os.path.isfile(path):
        fp = open(path, 'r')
        body = ""  
        body += "HTTP/1.1 200 OK\r\n"
        body += "Date: " + format_date_time(time.mktime(datetime.datetime.now().timetuple())) + "\r\n"
        body += "Server: David Ho's web server\r\n" 
        body += "Connection: close\r\n"
        body += "Content-Type: text/html\r\n"
        body += "\r\n"
        body += fp.read()  
    else:
        body = "HTTP/1.1 404 Not Found\r\n"
        body += "Date: " + format_date_time(time.mktime(datetime.datetime.now().timetuple())) + "\r\n"
        body += "Server: David Ho's web server\r\n" 
        body += "Connection: close\r\n"
        body += "Content-Type: text/html\r\n"
        body += "\r\n"
        body += "<html><head><title>404 Not Found</title></head><body><h1>Not Found</h1><p>The requested URL was not found on this server.</p></body></html>"
    client.send(body.encode())
    client.close()
