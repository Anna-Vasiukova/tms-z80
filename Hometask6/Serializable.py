from abc import abstractmethod


class Field(object):
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = self.convert(value)

    @abstractmethod
    def convert(self, value): ...

    @abstractmethod
    def dump(self, value): ...

    @abstractmethod
    def load(self, dat: bytes): ...


class Integer(Field):
    def dump(self, value: int):
        return value.to_bytes(4, 'big')

    def load(self, dat: bytes):
        return int.from_bytes(dat[0:4], 'big'), 4

    def convert(self, value):
        if isinstance(value, int):
            return value
        if isinstance(value, float):
            x = int(value)
            if x != value:
                raise ValueError()
            return x
        raise ValueError()


class Float(Field):
    def convert(self, value):
        if isinstance(value, float):
            return value
        if isinstance(value, int):
            return float(value)
        raise ValueError()

    def dump(self, value):
        from struct import pack
        return pack('>d', value)

    def load(self, dat: bytes):
        from struct import unpack
        return unpack('>d', dat[0:8])[0], 8


class String(Field):
    def convert(self, value):
        if isinstance(value, str):
            return value
        raise ValueError()

    def dump(self, value: str):
        dat = value.encode('utf-8')
        n = len(dat)
        return n.to_bytes(2, 'big', signed=False) + dat

    def load(self, dat: bytes):
        n = int.from_bytes(dat[0:2], 'big', signed=False)
        value = dat[2:2+n].decode('utf-8')
        return value, 2+n


class Serializable(object):
    def dump(self) -> bytes:
        cls = self.__class__
        desc = {}
        for base in reversed(cls.__mro__):
            for key, value in base.__dict__.items():
                if isinstance(value, Field):
                    desc[key] = value
        result = b''
        for field in desc.values():
            result += field.dump(field.__get__(self, cls))
        return result

    @classmethod
    def load(cls, dat: bytes):
        desc = {}
        for base in reversed(cls.__mro__):
            for key, value in base.__dict__.items():
                if isinstance(value, Field):
                    desc[key] = value
        obj = {}
        for key, value in desc.items():
            val, n = value.load(dat)
            obj[key] = val
            dat = dat[n:]
        dic = Test.__new__(Test)
        dic.__dict__.update(obj)
        return dic


class Test(Serializable):
    x = Integer()
    _y = Float()
    z = String()

    def __init__(self, x: int, y: float, z: str):
        self.x: int = x
        self._y: float = y
        self.z: str = z

    def __eq__(self, other):
        if not isinstance(other, Test):
            return False
        return self.x == other.x and self._y == other._y and self.z == other.z


a = Test(1, 2.5666, 'abc')
print(a.__dict__)
data = a.dump()
print(data)
b = Test.load(data)
print(b.__dict__)
print(a == b)
