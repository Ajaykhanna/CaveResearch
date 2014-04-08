import numpy as np
import sympy as sym
import math
from DiffFreqs import factorial

def laguerre(a, n):
    """
        Generates the nth laguerre polynomial with superscript a
        using the Rodrigues formula.
    """
    # function = lambda x: ((x ** -a)*(math.exp(x))/(math.factorial(n))) #incomplete
    x = sym.Symbol('x')
    subFunction = (sym.exp(-x) * (x ** (a+n))).diff(x, n)
    L = ((x ** -a)*(sym.exp(x))/(sym.factorial(n))) * subFunction
    L = sym.simplify(L)
    #print "Laguerre", L
    l = sym.lambdify(x, L)
    return l

def sameFreqOverlap(n, m, w_wavenumbers, deltaQ):
    """
        n must be greater than m, w_wavenumbers is the frequency in wavenumbers
        deltaQ is the change in normal coordinate in bohr.
    """
    w = w_wavenumbers/8065.5/27.2116
    # F is the (massless) force constant for the mode
    F = w ** 2

    # Convert dQ from amu to multiples of electron mass:
    convertedQSquared = deltaQ**2/(6.02214*(10**23) * 9.1094*(10**-28))
    
    # X is defined as such in Siders, Marcus 1981
    X = (F * (convertedQSquared)) / ( 2 * w)
    
    L = laguerre(n-m, m)
    exp1 = (float(n)-m)/2
    exp2 = -X/float(2)
    P = ((X**(exp1) * (factorial(m)/float(factorial(n))))* np.exp(exp2) * L(X))
    return P
