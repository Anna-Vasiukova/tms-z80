class Readonly(object):
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        return instance.__dict__['_Test__val']

    def __set__(self, instance, value):
        raise AttributeError


class Test(object):
    def __init__(self):
        self.__val = 1

    @Readonly
    def val(self):
        return self.__val


test = Test()
print(test.val)  # OK, выводит 1
test.val = 2  # AttributeError
