import math
from Hermite import *

def factorial(n):
    """ Implements factorial because python 2.5 does not have it yet.
    """
    if n == 0: return 1
    else: return reduce(lambda x, y: x*y, range(1, n+1))

def diffFreqOverlap(Ln, Lm, deltaQ):
    """ Ln and Lm are lists where L[0] is the state number, L[1]
        is the frequency in wavenumbers.
        deltaQ is the change in normal coordinate (in bohr)
        Ln[1] must be less than Lm[1]
    """
    n = Ln[0]
    m = Lm[0]
    wn_wavenumbers = Ln[1]
    wm_wavenumbers = Lm[1]
    wn = wn_wavenumbers/8065.5/27.2116
    wm = wm_wavenumbers/8065.5/27.2116
    f = wn/wm
    w = wm
    
    # F is the (massless) force constant for the mode. But which w?
    F = w ** 2
    
    # X is defined as such in Siders, Marcus 1981 Average frequency?
    X = (F * deltaQ**2) / ( 2 * w)
    
    P0 = (-1)**(m+n) # Should data be alternating plus minus?
    P1 = math.sqrt(2*math.sqrt(f)/(1.0+f))
    P2 = ((2**(m+n) * factorial(m) * factorial(n))**(-0.5)
          * math.exp(-X*f/(1.0+f)))
    P3 = ((1-f)/(1+f))**((float(m)+n)/2.0)
    
    l = min(m,n)
    P4 = 0
    for i in range(l+1):
        #In Siders and Marcus's 'F_n(x)' is equal to my G(x)
        G = iHermite(n-i)
        H = DHermite(m-i)
        P4 += ((factorial(m)*factorial(n) /
                (float(factorial(i))*float(factorial(m-i))*float(factorial(n-i)))) *
               (4*math.sqrt(f)/(1-f))**i
               * H(math.sqrt(2*X*f/(1-f**2)))
               * G(f*math.sqrt(2*X/(1-f**2)))
               )
    answer = P0*P1*P2*P3*P4
    return answer

def genIntensities( deltaE, deltaQ, w_wavenumbers, wprime_wavenumbers):
    """ wprime must be greater than w"""
    wprime = wprime_wavenumbers/8065.5/27.2116
    w = w_wavenumbers/8065.5/27.2116
    intensityFunction = lambda n: (diffFreqOverlap([n, wprime_wavenumbers], [0, w_wavenumbers], deltaQ))**2
    intensities = map(intensityFunction, range(0,11))
    return intensities

def genEnergies(deltaE, w_wavenumbers, wprime_wavenumbers):
    wprime = wprime_wavenumbers/8065.5/27.2116
    w = w_wavenumbers/8065.5/27.2116
    energyFunction = lambda n: (deltaE + (n+0.5)*(wprime) - 0.5*w)
    energies = map(energyFunction, range(0, 11))
    return energies

