from socket import socket, AF_INET, SOCK_STREAM, IPPROTO_TCP, SHUT_WR
from select import select

server = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)
server.bind(('127.0.0.1', 80))
server.listen(1)
s, remote = server.accept()
s.setblocking(False)
server.close()

select([s], [], [])
data = s.recv(1000)

print(data)

with open('pic.jpg', 'rb') as file:
    data = b'HTTP/1.1 200 OK\r\n' \
           b'Content-Type: image/jpeg\r\n' \
           b'\r\n'
    s.send(data)
    s.send(file.read())

s.shutdown(SHUT_WR)
s.close()

