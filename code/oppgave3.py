from oppgave2 import generateA
import numpy as np
from scipy.linalg import solve
import math

n = 10

length = 2.0
width = 0.3
thickness = 0.03
density = 480.0  # kg/m^3
g = -9.8  # gravity, m/s^2
E = 1.3 * pow(10, 10)  # N/m^2
I = (width * pow(thickness, 3)) / 12.0
f = - density * width * thickness * g
h = length/n

matrixB = [((pow(h, 4)/(E * I))) * f] * n
matrixA = generateA(n)

matrixY = solve(matrixA, matrixB)
print(matrixY)
