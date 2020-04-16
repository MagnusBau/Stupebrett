from oppgave3 import solve_3
# konstanter
length = 2.0
width = 0.3
thickness = 0.03
density = 480.0  # kg/m^3
g = 9.8  # tyngdekraft, m/s^2
E = 1.3 * pow(10, 10)  # N/m^2
I = (width * pow(thickness, 3)) / 12.0
f = - density * width * thickness * g

# Den eksakte løsningen
correct_solution = (f / (24 * E * I)) * pow(length, 2) * (pow(length, 2) - 4 * length * length + 6 * pow(length, 2))

# Loop for å regne ut en tilnærming for n = 20, 40 ... 2 * 10^(11), og så sammenligne det med den eksakte løsningen for å finne feilen.
# Printer også kondisjonstallet til matrisen A
for j in range(1, 12):
    n = 10 * pow(2, j)
    approx, kondisjonstall = solve_3(n)
    print(kondisjonstall)
    approx = approx[n-1]
    error = correct_solution - approx
    print(error)
