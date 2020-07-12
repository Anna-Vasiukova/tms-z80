from Hometask7_client_server import Client_module
import json

new_user = {
    'id': 3,
    'name': 'Ray',
    'messages': [3]
}

new_message = {
    'id': 3,
    'author': 3,
    'text': 'Hello, Ray!'
}


request = 'POST /messages/1/text HTTP/1.0\r\n\r\n' + json.dumps(new_message)
print(Client_module.request(request, '127.0.0.1', 8000))


request = 'GET /messages HTTP/1.0\r\n\r\n'
print(Client_module.request(request, '127.0.0.1', 8000))
