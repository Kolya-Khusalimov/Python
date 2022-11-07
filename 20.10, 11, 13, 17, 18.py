import numpy as np

import numpy.random as rnd
#20.10
N = 10
a = np.arange(N)
a = rnd.rand(N)
print(a, a.size)
K = 5
b = a[K:]
c = a[:K]
print(b)
print(c)
d1 = np.vstack([b, c])
d2 = np.hstack([b, c])

print(d1, d1.size, d1.shape)
print(a, a.shape)

def inputMatr(n):
    #A = np.ones((n,n), np.float32)
    M = n*n
    print(M)
    A = np.array(M)
    A.shape = (n, n)
    print(A)
    for i in range(n):
        for j in range(n):
            x = float(input(f"a{i}{j}"))
            A[i, j] = np.array(x, dtype = np.float32)
    return A

A = inputMatr(2)
print(A)


vect = np.zeros(A.shape[0])
for i in range(A.shape[0]):
    for j in range(A.shape[1]):
        vect[i] += abs(A[i, j])

b = np.max(vect)
print(b)

def sum_abs(v):
    s = 0
    for x in v:
        s += abs(x)
    return s

b = np.max(np.sum(np.abs(A), axis = 0 ))


def is_ortol(x):
    for i in range(x.shape[0]):
        for j in range(x.shape[0]):

            prod = np.dot(x[i], x[j])
            if i == j:
                if not np.isclose(prod, 1):
                    return False
            else:
                if not np.isclose(prod, 0):
                    return False
    return True

def is_ortol2(x):
    prod = np.dot(x, x.T)
    eye = np.eye(x.shape[0])
    return np.all(np.neg(np.isclose(eye, prod)))

if __name__ == "__main__":

    x = np.eye(3)
    print(x)
    print(is_orto1(x))
    print(is_orto2(x))

    y = np.array(
        [[1, 2, 3], [3, 2, 1], [1, 1, 1]], dtype = np.float32)
    print(is_orto1(y))
    print(is_orto2(y))

#20.11
def matrix(x):
    magic_matrix = True
    for i in range(x.shape[1]):
        if np.sum(x[:i]) != np.sum(x[:1]) or np.sum(x[:i]) != np.sum(x[:1]):
            magic_matrix = False
            break
        else:
            pass
    return magic_matrix
if __name__ == '__main__':
    print(matrix(np.array([[5,5,5],[5,5,5],[5,5,5]])))
    print(matrix(np.array([[5,5,5],[5,8,5],[6,5,5]])))

#20.11
matrix = numpy.array([
    [4, 9, 2],
    [3, 5, 7],
    [8, 1, 6]
])

cols_sum = numpy.sum(matrix, axis = 0)
rows_sum = numpy.sum(matrix, axis = 1)

r = numpy.concatenate((cols_sum, rows_sum), axis=0)
r = r == r[0]
r = r.all()

print('Це магічний квадрат' if r else 'Це НЕ магічний квадрат ')

#20.13
def inputPoints():
    n = int(input("n= "))
    ar = []
    for i in range(n):
        x = float(input("x= "))
        y = float(input("y= "))
        ar.append((x, y))
    return ar

def dist(i, j, x, y):
    global x, y
    return (x[i] - x[j])**2 + (y[i]- y[j])**2


if __name__ == '__main__':
    pts = inputPoints()

    x = np.array([it[0] for it in ar])
    y = np.array([it[1] for it in ar])

    for x1, y1 in zip(x, y):
        for x2, y2 in zip(x, y):
            z = np.sqrt((x1 - x2)**2 + (y1 - y2)**2)


    zs = np.array()
    xs = np.array()
    ys = np.array()

    mas = np.array(n*n*3)
    mas.reshape(3, n*n)
    for i in range(x.size()):
        z = np.sqrt(((x - x[i])**2) + (y - y[i])**2)
        zs = np.vstack(zs, z)
        x_ = np.arange(x.size())
        y_ = np.ones(x.size()) * i
        xs = np.vstack(xs, x_)
        ys = np.vstack(ys, y_)

    mas[0, :] = xs
    mas[1, :] = ys
    mas[2, :] = zs

    m = np.max(mas, axis = 2)
    ind = np.argmax(mas, axis = 2)
    print("Max ({}{}) = {}".format(ind[0], ind[1], m))


#20.17
import numpy.random as rnd
N = 1000
x = rnd.uniform(-1, 1, N)
y = rnd.uniform(-1, 1, N)
z = x**2 + y**2<=1
k = z[z==1]
PI = k.size()/N * 4
prinit("pi {}".format(PI))

#20.18
import numpy.random as rnd
N = 10
x = rnd.randint(6, size = (N, 4))
print(x)
s = np.sum(x, axis = 1)
k = len(s [s <= 9])
Wins = k*10 / N
print(Wins)