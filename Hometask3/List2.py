array = list(map(int, input('Введите список чисел: ').split()))
# старайся давать переменным короткие, но более содержательные названия
# через некоторое время ты даже сама потом такой код прочитать не сможешь
k, v = None, 0
counter = {}
for value in array:
    count = counter.get(value, 0) + 1
    if count > v:
        k, v = value, count
    counter[value] = count

print(f'{k} встречается {v} раз')
#  1. ты проходишь по set - это O(N)
#  2. в каждой итерации ты вызываешь count - это еще O(N)
#  сложность получится O(N^2), хотя можно было решить за O(N)
#  но в целом, верно
