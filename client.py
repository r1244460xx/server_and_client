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
    httpRequest = ("GET / HTTP/1.1\r\n"
                    "Host: localhost:1234\r\n5"
                    "Connection: keep-alive\r\n"
                    "Cache-Control: max-age=0\r\n"
                    "DNT: 1\r\n"
                    "Upgrade-Insecure-Requests: 1"
                    "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36\r\n"
                    "Sec-Fetch-Mode: navigate\r\n"
                    "Sec-Fetch-User: ?1\r\n"
                    "Accept: text/html,application/xhtml+xml,application/xml;()q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3\r\n"
                    "Sec-Fetch-Site: none\r\n"
                    "Accept-Encoding: gzip, deflate, br\r\n"
                    "Accept-Language: zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7\r\n")     
    sk.send(httpRequest.encode())
    print(sk.recv(1024))
except socket.error:
    print("Fail to build connection")
    sk.close()