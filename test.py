from sympy import symbols, Eq, solve

x,y = symbols('x y')
c = 10
a = Eq(2*c*x + y, 2*c)
b = Eq(x - 2*y, 3)
print(solve((a,b), (x,y)))