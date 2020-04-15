
from oppgave4c import derivert
import numpy as np
from numpy import linalg as la
from oppgave2 import generateA

E = 1.3 *pow(10, 10)
w = 0.30
d = 0.03
tetthet = 480.0
L = 2.0
I = w*pow(d, 3)/12.0
g = -9.81
f = tetthet*w*d*g
h = L / 0.2


ones = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
compare = f/(E*I) * ones

print("\n\noppgave d \n")
print(compare)

ans = derivert(10)
A = generateA(int(h))

foroverfeil = la.norm(ans-compare, np.inf)
relForoverfeil = foroverfeil / la.norm(ans, np.inf)
feilforstørrelse = relForoverfeil / pow(2, -52)
kondisjonstall = la.cond(A)
print("foroverfeil\n", foroverfeil)
print("relativ foroverfeil\n", relForoverfeil)
print("feilforstørrelse\n", feilforstørrelse)
print("kondisjonstall\n", kondisjonstall)

