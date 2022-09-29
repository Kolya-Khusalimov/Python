def _type(typ):
    def type_checker(fun):
        def _type_cheker(*args):
            for i in args:
                if type(i) == typ:
                    continue
                else:
                    raise TypeError
            return fun(*args)
        return _type_cheker
    return type_checker

@_type(int)
def func(a, b, c):
    return print((a + b + c) / 3)

if __name__ == '__main__':
    try:
        func(1, 0, 5)
        func(1.3, 0, 5)
    except TypeError:
        print("Wrong type!")