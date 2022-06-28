from numpy import arctan

def function(x):
    return arctan(x)

def n_teylor(x, n):
    return  (-1)**(n-1) * x**(2*n - 1) / (2*n - 1)

def sum_of_taylor(x, n):
    res = 0
    for i in range(1,n+1,1):
        res += n_teylor(x, i)
    return res

def abs_error(dx, x):
    return abs(dx - x)

def relative_error(dx, x):
    return abs_error(dx, x) / dx