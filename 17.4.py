def mydec(f):
    def _mydec(*args):
        for i in args:
            if  not type(i) is str:
                raise TypeError
        res = f(*args)
        return res
    return _mydec
    
    
@mydec  
def func(*args):
    lst = []
    for i in args:
        lst = lst + i.split(" ")
    lst = set(lst)
    return list(lst)

if __name__ == '__main__':
    print("{}".format(func("h e l l o", "w o r l d")))

    try:
        func(1, 2, 3)
    except TypeError:
        print("Caught an exception! Not str!")
