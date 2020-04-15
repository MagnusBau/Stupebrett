import scipy as sp
from scipy.sparse import spdiags
from scipy.sparse import lil_matrix
from scipy.sparse import csr_matrix
g = -9.81
E = 1.3 * 10**10
I = 67.5 * 10**(-8)
L = 2.0
w = 0.3
d = 0.03
tetthet = 480
f = -480 * w * d * g

def genA(n):
    ones = sp.ones(n)
    A = spdiags([ones, -4 * ones, 6 * ones, -4 * ones, ones], [-2, -1, 0, 1, 2], n, n)
    A = lil_matrix(A)
    A2 = csr_matrix([[16, -9, (8 / 3), -(1 / 4)],
    [(16 / 17), -(60 / 17), (72 / 17), -(28 / 17)],
    [-(12 / 17), (96 / 17), -(156 / 17), (72 / 17)]])
    A[0, 0:4] = A2[0, :]
    A[n - 2, n - 4:n] = A2[1, :]
    A[n - 1, n - 4:n] = A2[2, :]
    return A

def genYe(x):
    return (f / (24 * E * I)) * (x ** 2) * (x ** 2 - 4 * L * x + 6 * (L ** 2))


def ye():
    z = [0 for x in range(0, 10)]
    start = 0
    for i in [float(j) / 10 for j in range(2, 22, 2)]:
        z[start] += genYe(i)
        start += 1
    return z


def derivert(n):
    A = genA(n)
    h = L / n
    ye1 = ye()
    return (1 / h ** 4) * A * ye1

print("Numerisk fjerdederiverte: ")
print(derivert(10))



