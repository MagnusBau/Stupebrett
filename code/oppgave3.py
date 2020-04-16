from oppgave2 import generateA
import numpy as np
from scipy.linalg import solve

#Gitte bjelkeparametre.
length = 2.0
width = 0.3
thickness = 0.03
density = 480.0  # kg/m^3
# Andre konstanter.
g = 9.8  # gravity, m/s^2
E = 1.3 * pow(10, 10)  # Materialkonstanten N/m^2
I = (width * pow(thickness, 3)) / 12.0 #Arealmomentet.
f = - density * width * thickness * g

#L�sning p� Ay=b med st�rrelse (n)
def solve_3(n):
	#Deler bjelkens lengde s� alle segmentene er like.
    h = length / n
	#Genererer b�ndmatrise (A matrisen)
    matrixA = generateA(n)
	#Genererer b-matrisen.
    matrixB = np.array([[(pow(h, 4) / (E * I)) * f]] * n)
	#L�ser for Y basert p� A og B.
    matrixY = solve(matrixA, matrixB)
	#Finner kondisjonstallet.
    kondisjonstall = np.linalg.cond(matrixA)
	#Returnerer l�sningen og kondisjonstallet.
    return matrixY, kondisjonstall



# print(matrixY)
# # Check solution
# print("Solution: " + str(np.allclose(np.dot(matrixA, matrixY), matrixB)))