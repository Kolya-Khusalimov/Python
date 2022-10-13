def types_check(cls):
    constructor = cls.__init__

    def __init__(self, *args, **kwargs):
        constructor(self, *args, **kwargs)
        print("INITY", args)
        for name, value in self.__dict__.items():
            if not isinstance(value, cls._field_type[name]):
                raise TypeError(f" Attribute {name} is not {cls._field_type[name]}")
    cls.__init__ = __init__
    return cls

@types_check
class CheckClass:
    _field_type = {"x": int, "y": float, "s": str}

    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.s = s

    def __str__(self):
        return f" {self.x}, {self.y}, {self.s}"

if __name__ == '__main__':
    s1 = CheckClass(1, 2.44, "fdfdsafsda")
    print(s1)
    try:
        s2 = CheckClass(1, 2.44, "fdfdsafsda")
        print(s2)

    except TypeError as e:
        print("Exception", e.show())