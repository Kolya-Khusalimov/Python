import numpy as np
import matplotlib.pyplot as plt

def seq(n):
   res =  (n* (n**(1/7)) + (16 * (n**8) + 5) ** (1/4)) / ((n+n**(1/3)) * ((n**5 - 1) ** (1/5)))
   return res

def check_seq(a, b, eps):
    c = abs(a - b) < eps
    k = -1
    for i in range(c.size):
        if c[i] == True:   #if abs(a - b) < eps
            k = i
            break

    if k != -1:
        c1 = c[k: c.size]
        if np.all(c1):
            print("Sequence is convergent after element ", k)
            return k
    else:
        print("Sequence is not convergent")

def graphik():
    ax = plt.gca()
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data', 0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data', 0))

if __name__ == '__main__':
    eps = 0.1
    b = 2
    n = int(input("Number of elements: "))
    n1 = np.array([i for i in range(2, n)])
    x = [seq(i) for i in range(2, n)]
    a = np.array(x)

    k = check_seq(a, b, eps)

    b1 = np.ones(n1.size)*b
    graphik()
    plt.plot(n1, a)
    plt.ylabel("n")
    plt.ylabel("a(n)")
    plt.plot(b1, 'g')
    plt.plot(n1, b1 - eps, '--r')
    plt.plot(n1, b1 + eps, '--r')
    plt.show()