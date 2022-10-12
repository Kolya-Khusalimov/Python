import numpy as np
import matplotlib.pyplot as plt
from math import cosh,factorial
from matplotlib import animation

def movespinesticks():
    ax = plt.gca()
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data',0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data',0))

def fun(x):
    try:
        y = cosh(x)
    except Exception as e:
        print('Exception handling', e)
        n = x.size
        y = np.ones(n)
        for i in range(n):
            y[i] = cosh(x[i])
    return y

def aproxF(x,k):
    s=np.ones(x.size)
    for i in range(2,k,2):
        s += x**i/factorial(i)
    return s

fig = plt.figure()
ax = plt.axes(xlim = (-3, 3),ylim = (-3, 3))
line,= ax.plot([], [], lw = 1)

def init():
    line.set_data([], [])
    return line,

def animate(k):
    x = np.linspace(-3,3,100)
    y = aproxF(x, k)
    line.set_data(x, y)
    return line,

movespinesticks()
anim = animation.FuncAnimation(fig, animate, init_func = init,
                               frames = 10, interval = 150, blit = True)


xx = np.linspace(-3, 3, 100)
s = fun(xx)
plt.plot(xx,s,'r')
plt.show()