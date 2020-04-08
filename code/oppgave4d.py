
from oppgave4c import numFjerdeDer
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


ones = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
comp = f/(E*I) * ones

print("\n\noppgave d \n")
print(comp)

ans = numFjerdeDer()

print(la.norm(ans-comp, np.inf))
