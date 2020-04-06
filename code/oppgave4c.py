
from oppgave2 import generateA
import numpy as np
from numpy import linalg as la

E = 1.3 *pow(10, 3)
w = 0.30
d = 0.03
tetthet = 480
L = 2
I = w*pow(d, 3)/12
g = -9.81
f = tetthet*w*d*g
h = L / 0.2

def eksaktLos(x):
    return (f/(24*E*I))*pow(x,2)*(pow(x,2) - 4*L*x + 6*pow(L, 2))


y = np.array([eksaktLos(0.2)])


for i in range(2, 11, 1):
    x = 0.2 * i
    y = np.append(y, [eksaktLos(x)])


A = generateA(int(h))

ans = np.dot(A, y) / pow(h, 4)

print(ans)

ones = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
comp = f/(E*I) * ones

print(comp)

print(la.norm(ans-comp, np.inf))


