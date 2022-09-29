def trace(f):
    depth = 0
    def _trace(*args, **kw):
        nonlocal depth
        depth += 1
        print("Enter")
        print("Depth: ", depth)
        print("Arguments: ", *args, **kw)
        res = f(*args, **kw)
        print("Exit", '\n')
        print("Depth: ", depth)
        print("result: ", res)
        depth -= 1
        return res
    return _trace

@trace
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


@trace
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


if __name__ == '__main__':
    print(fib(5))
    print(fact(6))
