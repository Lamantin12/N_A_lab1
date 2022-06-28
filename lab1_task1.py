from sys import float_info

def MachineEpsilon():
    """
    Function counting machine epsilon

    :return: float number
        Machine epsilon
    """
    eps = 1.0
    while (1.0 + eps) != 1.0 :
        eps /= 2
    return eps

def MachineNull():
    """
    Function counting machine null

    :return: tuple(float,int)
        Machine Null and power of 2 to reach it
    """
    X0 = 1
    t = 0
    buf = 2
    while X0 != 0 :
        X0 /= 2
        buf /= 2
        t +=1
    return buf, t

def MachineInf():
    """
    Function counting machine null

    :return: tuple (float,int)
        Machine Infinity and power of 2 to reach it
    """
    Xinf = 1.0
    t = 0
    buf = 0.5
    while Xinf <= float_info.max:
        Xinf *= 2
        buf *= 2
        t += 1
    return buf, t
