from Hometask7_client_server import Client_module
import json

new_user = {
    'id': 3,
    'name': 'Ray',
    'messages': []
}
new_message = {
    'id': 3,
    'author': 3,
    'text': 'Hello, Ray!'
}

request = 'POST /users HTTP/1.0\r\n\r\n' + json.dumps(new_user)
print(Client_module.request(request, '127.0.0.1', 80))

request = 'GET /users HTTP/1.0\r\n\r\n'
print(Client_module.request(request, '127.0.0.1', 80))
