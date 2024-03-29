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
p = 100.0  # kg/m
Lp = length / np.pi
personWeight = 50.0
personLength = 0.3
# Correct_solution må også regne ut funksjonen for sinushaugen.
correct_solution = (f / (24 * E * I)) * pow(length, 2) * (pow(length, 2) - 4 * length * length + 6 * pow(length, 2)) \
                   - (((g * p * length) / (E * I * np.pi)) * (((pow(Lp, 3)) * np.sin(np.pi)) - (pow(length, 3) / 6) + (pow(
    length, 3) / 2) - (pow(length, 3) / pow(np.pi, 2))))


# vi trenger en funksjon for s(x) for å løse f(x) + s(x)
def solve_s(x):
    s = - p * g * np.sin((np.pi/length) * x)
    return s


# Vi bruker solve_s(x) i matrixB, returnerer matrixY og kondisjonstallet
def solve_6(n):
    h = length / n
    matrixA = generateA(n)
    matrixB = np.array([[(pow(h, 4) / (E * I)) * f]] * n)
    for i in range(len(matrixB)):
        matrixB[i] = [(pow(h, 4) / (E * I)) * (f + solve_s(h * i))]

    matrixY = solve(matrixA, matrixB)
    kondisjonstall = np.linalg.cond(matrixA)
    return matrixY, kondisjonstall


# Skriver ut tilnærming, kondisjonstall og feil for utvalgte n-verdier
for j in range(1, 12):
    n = 10 * pow(2, j)
    approx, kondisjonstall = solve_6(n)
    print(approx[n-1])
    approx = approx[n - 1]
    error = correct_solution - approx
    print(kondisjonstall)
    print(error)
    print("\n")
