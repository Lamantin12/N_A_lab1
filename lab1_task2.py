from numpy import arctan, float64, format_float_scientific

def function(x):
    return arctan(x)

def n_teylor(x, n):
    return (-1)**(n-1) * x**(2*n - 1) / (2*n - 1)

def sum_of_taylor(x, n):
    res = 0
    for i in range(1,n+1,1):
        res += n_teylor(x, i)
    return res

def abs_error(dx, x):
    return abs(dx - x)

def relative_error(dx, x):
    return abs_error(dx, x) / dx

def N_reaching_error_in_dot(dot, epsilon):
    """
    :param dot: dot where we find N'th sum that reaches error
    :param epsilon: acceptable error in dot
    :return: int n
            number of elements in sum that fits in error
    """
    Sum = n_teylor(dot, 1)
    n = 2
    buf_taylor_element = n_teylor(dot, 2)
    while abs(buf_taylor_element / Sum) > epsilon:
        Sum += buf_taylor_element
        n += 1
        buf_taylor_element = n_teylor(dot, n)
    return n


def ROUND(x, t=4):
    return float64(format_float_scientific(x, precision=t))

def S_n_rounded_el(x, n):
    res = 0
    for i in range (1,n+1,1):
        res += ROUND(n_teylor(x, i), 6)
        res = ROUND(res, 6)
    return res
def S_n_rounded(x, n):
    res = x.copy()
    for i in range(len(x)):
        res[i] = S_n_rounded_el(x[i], n)
    return res
