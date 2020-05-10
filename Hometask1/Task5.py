s = input()
tokens = s.split(' ')

for i in range(len(tokens) - 1, -1, -1):
    token = tokens[i]
    if token == '*':
        a = tokens[i - 1]
        b = tokens[i + 1]
        tokens[i - 1:i + 2] = [float(a) * float(b)]
    elif token == '/':
        a = tokens[i - 1]
        b = tokens[i + 1]
        tokens[i - 1:i + 2] = [float(a) / float(b)]

for i in range(len(tokens)-1, -1, -1):
    token = tokens[i]
    if token == '+':
        a = tokens[i - 1]
        b = tokens[i + 1]
        tokens[i - 1:i + 2] = [float(a) + float(b)]
    elif token == '-':
        a = tokens[i - 1]
        b = tokens[i + 1]
        tokens[i - 1:i + 2] = [float(a) - float(b)]

print(tokens[0])
