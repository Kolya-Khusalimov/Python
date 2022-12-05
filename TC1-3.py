from threading import Thread
from time import sleep
import logging

#TC1

logging.basicConfig(level=logging.DEBUG)


class ThreadWithException(Thread):

    def init(self, target = None, args = (), kwargs = ()):
        super().init()

        self._f = target
        self._f_args = args
        self._f_kwargs = kwargs if kwargs else {}
        self._exception = None
        self._result = None

    def run(self):
        try:
            self._result = self._f(*self._f_args, **self._f_kwargs)
        except Exception as e:
            self._exception = e

    def get_result(self):
        return self._result

    def get_exception(self):
        return self._exception


def fact(n):
    result = 1
    for i in range(1, n + 1):
        logging.debug(f"Обчислення нерекурсивного факторіалу для {i}")
        result *= i
        logging.debug(f"Нерекурсивний факторіал для {i} дорівнює {result}")
        sleep(0)
    return result


def fact_rec(n):
    logging.debug(f"Обчислення рекурсивного факторіалу для {n}")
    if n == 0:
        result = 1
    else:
        result = n * fact_rec(n - 1)
    logging.debug(f"Нерекурсивний факторіал для {n} дорівнює {result}")
    sleep(0)
    return result


if name == "main":
    n = 40

    th1 = ThreadWithException(target = fact, args = (n, ))
    th2 = ThreadWithException(target = fact_rec, args = (n, ))
    th1.start()
    th2.start()

    for k in range(10):
        logging.debug("Tick {}".format(k))
        sleep(0)

    th1.join()
    th2.join()

    if th1.get_exception() is None:
        print("Потік 1 завершився успішно:", th1.get_result())
    else:
        print("Отримано виключення в потоці 1:", th1.get_exception())

    if th2.get_exception() is None:
        print("Потік 2 завершився успішно:", th2.get_result())
    else:
        print("Отримано виключення в потоці 2:", th2.get_exception())

#TC2

logging.basicConfig(level = logging.DEBUG)

T1 = 1
T2 = 2

q = Queue()
start = time()


def log(message: str):
    t = time() - start
    name = threading.current_thread().getName()
    logging.debug("[%6.3f] %s: %s", t, name, message)


def put(count, process_time):
    for i in range(count):
        sleep(process_time)
        message = f"ПОВІДОМЛЕННЯ {i} (створено о {time() - start:6.3f})"
        log(f"В чергу додано   {message}")
        q.put(message)


def get(count, process_time):
    for i in range(count):
        message = q.get()
        log(f"З черги отримано {message}")
        sleep(process_time)
        print(f"\"{message}\" оброблене на {time() - start:6.3f} секунді")


if name == "main":
    n = 10
    th1 = threading.Thread(name = "Put", target = put, args = (n, T1))
    th2 = threading.Thread(name = "Get", target = get, args = (n, T2))
    th1.start()
    th2.start()
    th1.join()
    th2.join()
    log("Кінець")

