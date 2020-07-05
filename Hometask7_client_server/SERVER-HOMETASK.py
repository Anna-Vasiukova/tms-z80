from Hometask7_client_server import server_module
from typing import List


class User(object):
    def __init__(self, id: int, name: str, messges: List[int]):
        self.id = id
        self.name = name
        self.messages = messges


class Message(object):
    def __init__(self, id: int, author: int, text: str):
        self.id = id
        self.author = author
        self.text = text


users = {
    1: User(1, 'Bob', [1]),
    2: User(2, 'Alice', [2])
}

messages = {
    1: Message(1, 1, 'Hello, Bob!'),
    2: Message(2, 2, 'Hello, Alice!')
}


def get_value(values, id, field):
    if id:
        obj = values.get(int(id), None)
        if not obj:
            return None
        if field:
            return getattr(obj, field, None)
        else:
            return obj.__dict__
    else:
        return [obj.__dict__ for obj in values.values()]


new_user = User(3, 'Ray', [3])
new_message = Message(3, 3, 'Hello, Ray!')


def set_value(values, id, field, value):
    if id:
        obj = values.get(int(id), None)
        if not obj:
            return 'HTTP/1.0 404 Not Found\r\n\r\n'
        if field:
            func = value.__dict__
            setattr(obj, field, func[field])
            obj = obj.__dict__
            return obj[field]
        else:
            obj.__dict__ = value.__dict__
            return obj.__dict__
    else:
        values[value.id] = value
        res = [obj.__dict__ for obj in values.values()]
        return res


def handler(request: str) -> str:
    import json
    import re
    lines = request.split('\r\n', 1)
    lines2 = lines[1]
    lines3 = lines2.split('\r\n\r\n')
    match = re.fullmatch(r'([A-Z]+) (/\S*) HTTP/(\d\.\d)', lines[0])
    if not match:
        return 'HTTP/1.0 400 Bad Request\r\n\r\n'
    method, path, version = match.group(1), match.group(2), match.group(3)
    if method not in ('GET', 'POST'):
        return 'HTTP/1.0 405 Method Not Allowed\r\n\r\n'

    match = re.fullmatch(r'/(users|messages)(?:/(\d+)(?:/([a-z]+))?)?', path)
    if not match:
        return 'HTTP/1.0 404 Not Found\r\n\r\n'
    var, id, field = match.group(1), match.group(2), match.group(3)
    if method == "GET":
        if var == 'users':
            result = get_value(users, id, field)
        else:
            result = get_value(messages, id, field)
        if result:
            return 'HTTP/1.0 200 OK\r\n\r\n' + json.dumps(result)
        else:
            return 'HTTP/1.0 400 Not Found\r\n\r\n'
    else:
        if var == 'users':
            new_result = set_value(users, id, field, new_user)
            return lines3[1].join(json.dumps(new_result))
        else:
            new_result = set_value(messages, id, field, new_message)
        if new_result:
            return lines3[1].join(json.dumps(new_result))
        else:
            return 'HTTP/1.0 404 Not Found\r\n\r\n'


server_module.serve(handler, '127.0.0.1', 80)
