
import sympy as sp
from scipy.misc import derivative

#Ayman abdoulrhman 311549737

def newton(f,a,b,e):
    xr =4
    for n in range(a,b):
        fxr = f(xr)
        if abs(fxr) < e:
            print('Found solution after',n, 'iterations.')
            return xr
        xr = xr - fxr / derivative(f,xr)

def secant(f,a,b,e):
    x0=0
    x1=4
    for n in range(a, b):
        x2 = x0 - (x1 - x0) * f(x0) / (f(x1) - f(x0))
        x0 = x1
        x1 = x2
        if abs(f(x2)) < e:
            print('Found solution after',n, 'iterations.')
            return x2

if __name__ == '__main__':
    p = lambda x: x ** 2 - x * 5 + 2
    a=0
    b=20
    print(newton(p,a,b,0.0001))
    print(secant(p,a,b,0.0001))





