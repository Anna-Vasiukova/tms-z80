# from socket import socket, AF_INET, SOCK_STREAM, IPPROTO_TCP, SHUT_WR
#
# s = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)
# s.connect(('google.kz', 80))
#
# data = b'GET / HTTP/1.0\r\n' \
#        b'Host: www.google.kz\r\n' \
#        b'\r\n'
#
# while data:
#     n = s.send(data)
#     data = data[n:]
# s.shutdown(SHUT_WR)
#
# data = b''
# while True:
#     x = s.recv(1000)
#     if x:
#         data += x
#     else:
#         break
#
# s.close()
# print(data)

from typing import List
import json


class User(object):
    def __init__(self, id: int, name: str, messges: List[int]):
        self.id = id
        self.name = name
        self.messages = messges


users = {
    1: User(1, 'Bob', [1]),
    2: User(2, 'Alice', [2])
}

new_user = User(3, 'Ray', [3])

for i in users.values():
    obj = i.__dict__
    print(obj)


def set_value(values, field, value):
    func = value.__dict__
    setattr(values, field, func[field])
    values = values.__dict__
    return values[field]



b = users[1]
print(b.name)
c = new_user.__dict__


# getattr(b, 'name')
b = set_value(b, 'messages', new_user)
print(b)

