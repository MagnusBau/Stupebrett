
import numpy as np
from oppgave2 import generateA
g = -9.81
E = 1.3 * 10**10
I = 67.5 * 10**(-8)
L = 2.0
w = 0.3
d = 0.03
tetthet = 480
f = -480 * w * d * g
h = L / 10

'''
Denne funksjonen gir en eksakt verdi for y ved på bruke løsningen for y gitt konstant f,
som ble oppgitt i løsningen.
'''
def eksaktLos(x):
    return (f/(24*E*I))*pow(x, 2)*(pow(x, 2) - 4*L*x + 6*pow(L, 2))


'''
Denne metoden lager vektor med h elementer. Hvert element er den eksakte løsningen for y(x)
med steglengde 0.2.
'''
def ye():
    ye = np.array([eksaktLos(0.2)])
    for i in range(2, 11, 1):
        x = 0.2 * i
        ye = np.append(ye, [eksaktLos(x)])
    return ye


'''
Denne funskjonen finner den fjerdederiverte ved å ta 1/h^4 * Ay
'''
def numFjerdeDer():
    y = ye()
    A = generateA(10)
    ans = -(1 / pow(h, 4)) * A.dot(y)
    return ans

print("ye: ")
print(ye())
print("Numerisk fjerdederiverte: ")
print(numFjerdeDer())



