import math
from func import *

# Modify-False-PostionMethod
# deviation
e = 10e-10


def sol(func, a, b):
    Fa = Fb = Fc = 0
    c_old = 0
    c_new = 0
    cnt = 0
    Fa = func(a)
    Fb = func(b)

    if Fa * Fb > 0:
        print("[X]{} Cannot solve, because f(a) * f(b) > 0".format(func.__name__))
        print("-----------------------------------")
        return False

    c_new = ((a*Fb)-(b*Fa))/(Fb-Fa)
    show_message(func.__name__, cnt, a, c_new, b)
    Fc = func(c_new)
    c_old = c_new

    if Fa * Fc < 0:
        b = c_new
    else:
        a = c_new
    c_new = ((a*Fb)-(b*Fa))/(Fb-Fa)

    while abs(c_old - c_new) >= e:
        cnt += 1
        show_message(func.__name__, cnt, a, c_new, b)
        Fa = func(a)
        Fb = func(b)
        c_new = ((a*Fb)-(b*Fa))/(Fb-Fa)
        Fc = func(c_new)
        c_old = c_new

        if Fa * Fc < 0:
            b = c_new
            Fa = Fa/2
        else:
            a = c_new
            Fb = Fb/2
        c_new = ((a*Fb)-(b*Fa))/(Fb-Fa)
    print("[{}]ANS: {}".format(func.__name__, c_new))
    print("-----------------------------------")


if __name__ == "__main__":
    sol(test, 0, 1.4)
    # sol(f1, -2, 2)
    # sol(f2, -5, 5)
    # sol(f3, -4, 3)
    # sol(f4, -6, 2)

