from Hometask7_client_server import Client_module


request = 'POST /users HTTP/1.0\r\n'\
          '\r\n' \
          '\r\n'
print(Client_module.request(request, '127.0.0.1', 80))
request = 'GET /users HTTP/1.0\r\n'\
          '\r\n' \
          '\r\n'
print(Client_module.request(request, '127.0.0.1', 80))
