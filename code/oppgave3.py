from oppgave2 import generateA
import numpy as np
from scipy.linalg import solve

length = 2.0
width = 0.3
thickness = 0.03
density = 480.0  # kg/m^3
g = 9.8  # gravity, m/s^2
E = 1.3 * pow(10, 10)  # N/m^2
I = (width * pow(thickness, 3)) / 12.0
f = - density * width * thickness * g


def solve_3(n):
    h = length / n
    matrixA = generateA(n)
    matrixB = np.array([[(pow(h, 4) / (E * I)) * f]] * n)
    matrixY = solve(matrixA, matrixB)
    kondisjonstall = np.linalg.cond(matrixA)
    return matrixY, kondisjonstall



# print(matrixY)
# # Check solution
# print("Solution: " + str(np.allclose(np.dot(matrixA, matrixY), matrixB)))