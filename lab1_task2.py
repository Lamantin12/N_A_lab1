from numpy import arctan, float64, format_float_scientific

def function(x):
    """
    Function counting arctan in dot x
    :param x:float
    :return:float
    """
    return arctan(x)

def n_teylor(x, n):
    """
    n-part of arctan teylor sum in dot x
    :param x:float
    :param n:int
    :return:float
    """
    return (-1)**(n-1) * x**(2*n - 1) / (2*n - 1)

def sum_of_taylor(x, n):
    """
    n-th teylor sum in dot x
    :param x:float
    :param n:int
    :return:float
    """
    res = 0
    for i in range(1,n+1,1):
        res += n_teylor(x, i)
    return res

def abs_error(dx, x):
    """
    Function counting absolute error between x and dx: |dx - x|
    :param dx:float
    :param x:float
    :return:float
    """
    return abs(dx - x)

def relative_error(dx, x):
    """
    Function counting relative error between x and dx: |dx - x|/dx
    :param dx:float
    :param x:float
    :return:float
    """
    return abs(dx, x) / dx

def N_reaching_error_in_dot(dot, epsilon):
    """
    Number of elements in Sum that fits in error epsilon in dot
    :param dot:float
    :param epsilon:float
    :return:n:int

    """
    Sum = n_teylor(dot, 1)
    n = 2
    buf_taylor_element = n_teylor(dot, 2)
    while abs(buf_taylor_element / Sum) > epsilon:
        Sum += buf_taylor_element
        n += 1
        buf_taylor_element = n_teylor(dot, n)
    return n


def ROUND(x, t = 4):
    """
    Function rounding mantissa of x to t signs
    :param x:float
    :param t:int
    :return:float
    """
    return float64(format_float_scientific(x, precision=t))

def S_n_rounded_el(x, n):
    res = 0
    for i in range (1,n+1,1):
        res += ROUND(n_teylor(x, i), 6)
        res = ROUND(res, 6)
    return res
def S_n_rounded(x, n):
    """
    n-th teylor sum in dot x where every part is rounded
    :param x:float
    :param n:int
    :return:float
    """
    res = x.copy()
    for i in range(len(x)):
        res[i] = S_n_rounded_el(x[i], n)
    return res
