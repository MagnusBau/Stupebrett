from oppgave2 import generateA
import numpy as np
from scipy.linalg import solve

# Gitte bjelkeparametre.
length = 2.0
width = 0.3
thickness = 0.03
density = 480.0  # kg/m^3
# Andre konstanter.
g = 9.8  # gravity, m/s^2
E = 1.3 * pow(10, 10)  # Materialkonstanten N/m^2
I = (width * pow(thickness, 3)) / 12.0 #Arealmomentet.
f = - density * width * thickness * g


# Losning paa Ay=b med storrelse (n)
def solve_3(n):
    # Deler bjelkens lengde saa alle segmentene er like.
    h = length / n
    # Genererer baandmatrise (A matrisen)
    matrixA = generateA(n)
    # Genererer b-matrisen.
    matrixB = np.array([[(pow(h, 4) / (E * I)) * f]] * n)
    # Loser for Y basert paa A og B.
    matrixY = solve(matrixA, matrixB)
    # Finner kondisjonstallet.
    kondisjonstall = np.linalg.cond(matrixA)
    # Returnerer losningen og kondisjonstallet.
    return matrixY, kondisjonstall


if __name__ == '__main__':
    matrixY, kondisjonstall = solve_3(10)
    print(matrixY)
