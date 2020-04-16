import sympy as sym

x= sym.Symbol('x')
E= sym.Symbol('E')
I= sym.Symbol('I')
L= sym.Symbol('L')
f= sym.Symbol('f')

# Definerer løsningen gitt i oppgaven
y = (f/(24*E*I))*x**2*(x**2 + 4*L*x + 6*L**2)

#D eriverer 4 ganger
for i in range(4):
    y = sym.diff(y, x)
print("y'''' = ", y)
print("Setter inn for y'''' i Euler-Bernouilli-likningen:  ", E * I * y)

