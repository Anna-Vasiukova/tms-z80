class Readonly(object):
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        return self.func(instance)

    def __set__(self, instance, value):
        return self.func(value)


class Test(object):
    def __init__(self):
        self.__val = 1

    @Readonly
    def val(self):
        return self.__val


test = Test()
print(test.val)  # OK, выводит 1
test.val = 2  # AttributeError
