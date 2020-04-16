from oppgave2 import generateA
import numpy as np
from scipy.linalg import solve
# Konstanter
length = 2.0
width = 0.3
thickness = 0.03
density = 480.0  # kg/m^3
g = 9.8  # tyngdekraften, m/s^2
E = 1.3 * pow(10, 10)  # N/m^2
I = (width * pow(thickness, 3)) / 12.0
f = - density * width * thickness * g
personWeight = 50.0
personLength = 0.3

# Denne funksjonen lager en matrise b der de første 1.7/2.0 delene er som i oppgave 5, og i den siste 0.3/2.0 delen
# blir f plusset med personens vekt * tyngdekraften.
# Returnerer siste innslag i løsningen y (Ay = b), som er hvor mye brettet bøyer seg på enden.
def solve_7(n):
    h = length / n
    personF = personWeight * -g / personLength
    matrixA = generateA(n)
    matrixB = np.array([[(pow(h, 4) / (E * I)) * f]] * n)
    for i in range(len(matrixB)):
        if h * i >= 1.7:
            matrixB[i] = [(pow(h, 4) / (E * I)) *( f + personF)]

    matrixY = solve(matrixA, matrixB)
    return matrixY[n-1]


# Regner ut solve_7 for n = 20, 40 ... 2*10^(9)
for j in range(1, 10):
    n = 10 * pow(2, j)
    print(solve_7(n))
