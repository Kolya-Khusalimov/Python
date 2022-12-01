import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#20.1(a)

@np.vectorize
def func01(n):
    return 3 / 2 * (1 - 1/pow(3, n+1)) * (n - 3) * pow(n, 1/n) / (2.0 * n + 5 / n)


def gety(f, x):
    n = x.size
    y = np.zeros(n)
    for i in range(n):
        y[i] = f(x[i])
    return y


def plot_seq(x, y, b = None, eps=0.01, forall = True):
    plt.figure(figsize = (12, 9))
    if b is None:
        plt.plot(x, y, ".b")
        return x[-1], y[-1]
    else:
        k = -1
        prev = False
        for i in range(y.size):
            if abs(y[i] - b) < eps:
                if not prev:
                    k = i
                    prev = True
            else:
                prev = False

        if not prev:
            return None, None


        begin = 0 if forall else k


        plt.plot(x[begin:], y[begin:], ".b")
        plt.plot(np.array((x[begin], x[-1])), np.array((b, b)), "-r")
        plt.plot(np.array((x[begin], x[-1])), np.array((b - eps, b - eps)), "--g")
        plt.plot(np.array((x[begin], x[-1])), np.array((b + eps, b + eps)), "--g")
        plt.xlabel("n")
        plt.ylabel("a(n)")
        plt.axis([x[begin], x[-1], b - eps*2, b + eps*2])
        return x[k], y[k]


if __name__ == "__main__":
    t = (1, 200, 1)
    x = np.arange(*t)
    y = func01(x)
    b = 0.75
    eps = 0.01
    x0, y0 = plot_seq(x, y, b, eps, True)
    print(x0, y0)
    plt.show()



#20.2

def circle():
    x1 = np.linspace(-1, 1, 1000)
    x2 = np.linspace(1, -1, 1000)
    y1 = -np.sqrt(1 - x1 * x1)
    y2 = np.sqrt(1 - x2 * x2)
    return np.hstack((x1, x2)), np.hstack((y1, y2))


def reg_poly(n):
    x = np.array([np.cos(i * 2 * np.pi / n) for i in range(n + 1)])
    y = np.array([np.sin(i * 2 * np.pi / n) for i in range(n + 1)])
    return x, y


def perimeter(x, y):
    return np.sqrt((x[0] - x[1]) ** 2 + (y[0] - y[1]) ** 2) * (x.size - 1)


fig = plt.figure()
plt.axes(xlim = (-2, 2), ylim = (-1.5, 1.5))
plt.plot(*circle(), "--r", lw = 6)
line, = plt.plot([], [], "-b", lw = 3)
plt.title("Circle and polygon")


def animate(i):
    x, y = reg_poly(2 ** (i + 2))
    print(perimeter(x, y) / 2)
    line.set_data(x, y)
    return line,


if __name__ == "__main__":
    anim = FuncAnimation(
        fig,
        animate,
        frames=15,
        interval=500,
        repeat=True
    )
    plt.show()



#20.3(a)

a = -4*np.pi
b = 4*np.pi
m = 20


x = np.linspace(a, b, int((b - a) * 50))

fig = plt.figure()
plt.axes(xlim = (a, b), ylim = (-5, 5))
line, = plt.plot([], [], "-b", lw = 3)


def func01_sin(x, n):
    s = x.copy()
    p = x.copy()
    for k in range(2, n + 1):
        p *= -x * x / ((2 * k - 2) * (2 * k - 1))
        s += p
    return s


def init():
    plt.plot(x, np.sin(x), "--r")
    return line,


def animate(i):
    y = func01_sin(x, i + 1)
    line.set_data(x, y)
    return line,


if __name__ == "__main__":
    anim = FuncAnimation(
        fig,
        animate,
        init_func = init,
        frames = m,
        interval = 2000,
        repeat = True)
    plt.show()