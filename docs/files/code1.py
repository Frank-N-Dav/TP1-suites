def u(n):
    return 3*n**2-4*n+1

from math import sqrt

def v(n):
    if n == 0:
        return -4
    else:
        return sqrt(2*v(n-1)+9)
    
def w(n):
    if n == 1:
        return 1/2
    else:
        return (n/(2*(n-1)))*w(n-1)