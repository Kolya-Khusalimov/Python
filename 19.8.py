import random
import time


def catch_exception(f):
    def func(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            with open("exception1.txt", 'w', encoding = "utf-8") as f1:
                f1.write(
                    f"Exception {e.__class__.__name__} was caught in method \"{f.__name__}\" with paremeters {args}")
    return func

def catch_exception_class(cls):
    for name, attr in cls.__dict__.items():
        if callable(attr) and not name.startswith('__'):
            catch_exception(attr)
    return cls

@catch_exception_class
def catch_exception_class(cls):
        for name, attr in cls.__dict__.items():
            if callable(attr) and not name.startswith('__'):
                setattr(cls, name, catch_exception(attr))
        return cls


class QueueEmptyError():
    def __init__(self, pname):
        self.pname = pname

    def __str__(self):

        return repr(self.pname) + ".Empty queue."

@catch_exception_class
class Queue(Exception):

    def __init__(self):
        self.x2 = 2
        self._lst = []

    @catch_exception
    def isempty(self):
        return len(self._lst) == 0


    @catch_exception
    def add(self, data):
        self._lst.append(data)


    @catch_exception
    def take(self):
        if self.isempty():
            raise QueueEmptyError("Take")
        data = self._lst.pop(0)
        return data

    def __del__(self):
        del self._lst



q = Queue()
q.take()
q.add()
q.isempty()
m = 0
z = 5
k = 0
t1 = 5
t2 = 3
T = 6
b = 0

for i in range(m):
    k += 1
    q.add(k)


for i in range(z):
    a = random.randint(0, t2)
    time.sleep(a)
    b += a
    j = q.take()
    print(f"Customer served! {j} {time.ctime(b)}")
    c = random.randint(0, t1)
    time.sleep(c)
    b += c
    if b >= T:
        break
    k = k+1
    q.add(k)
    print(f"+ one customer to queue {k} {time.ctime(b)}")


print("The rest of queue")
n = 0
while not q.isempty():
    h = q.take()
    n += 1
    print(f"{n} customers")