
from oppgave2 import generateA
import numpy as np
from numpy import linalg as la

E = 1.3 *pow(10, 10)
w = 0.30
d = 0.03
tetthet = 480.0
L = 2.0
I = w*pow(d, 3)/12.0
g = -9.81
f = tetthet*w*d*g
h = L / 0.2


def eksaktLos(x):
    return (f/(24*E*I))*pow(x, 2)*(pow(x, 2) - 4*L*x + 6*pow(L, 2))


def ye():
    ye = np.array([eksaktLos(0.2)])
    for i in range(2, 11, 1):
        x = 0.2 * i
        ye = np.append(ye, [eksaktLos(x)])
    return ye


def numFjerdeDer():
    y = ye()
    A = generateA(int(h))
    ans = (1 / pow(h, 4)) * A.dot(y)
    '''
    alt = []
    for i in range(0, 10):
        temp = 0
        for j in range(0, 10):
            temp += A[i][j] * y[j]
        alt.append(temp / pow(h, 4))
    print(alt)
    '''
    return ans


print("ye: ")
print(ye())

ans = numFjerdeDer()
print("Numerisk fjerdederiverte: ")
print(ans)


