from socket import socket, AF_INET, SOCK_STREAM, IPPROTO_TCP, SHUT_WR

s = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)
s.connect(('google.kz', 80))

data = b'GET / HTTP/1.0\r\n' \
       b'Host: www.google.kz\r\n' \
       b'\r\n'

while data:
    n = s.send(data)
    data = data[n:]
s.shutdown(SHUT_WR)

data = b''
while True:
    x = s.recv(1000)
    if x:
        data += x
    else:
        break

s.close()
print(data)
