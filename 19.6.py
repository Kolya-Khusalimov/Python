def trace(f):
    depth = 0
    def _trace(*args, **kwargs):
        nonlocal depth
        depth += 1

        print(f"Enter function {f.__name__}", end=":  ")
        print(f"Depth {depth}", end=", ")
        print(f"Positional {args}", end=", ")
        print(f"Key {kwargs}", end = "\n")
        res = f(*args, **kwargs)
        print(f"Exit function {f.__name__}", end=":")
        print(f"Depth {depth}", end = ", ")
        print(f"Result{res}", end = ", ")
        depth -= 1
        return res
    return _trace

def trace_class(cls):
    for name, attr in cls.__dict__.items():
        if name.startswith("__"):
            continue

        if not callable(attr):
            continue
        setattr(cls, name, trace(attr))
    return cls

class Simple:
    def __init__(self):
        pass

    def method1(self, x, y, z = 1):
        return x + y + z

    def method2(self, *args, **kwargs):
        if (kwargs):
            return method2(*args)

        for x in args:
            return 1

    def method3(self):
        return 0

if __name__ == "__main__":
    s = Simple()
    s.method1(1, 2, 3)
    s.method1(3, 4, 5, x = 1, y = 2)
    s.method3()