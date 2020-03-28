import math
from func import *

# False-Postion-Method
# deviation
e = 10e-10


def sol(func, a, b):
    # For first
    cnt = 0

    if func(a) * func(b) > 0:
        print("[X]{} Cannot solve, because f(a) * f(b) > 0".format(func.__name__))
        print("-----------------------------------")
        return False

    c_new = (a*func(b)-b*func(a))/(func(b)-func(a))
    show_message(func.__name__, cnt, a, c_new, b)
    if func(a) * func(c_new) < 0:
        b = c_new
    else:
        a = c_new

    c_old = c_new
    c_new = (a*func(b)-b*func(a))/(func(b)-func(a))

    while abs(c_old - c_new) >= e:
        cnt += 1
        show_message(func.__name__, cnt, a, c_new, b)
        if func(a) * func(c_new) < 0:
            b = c_new
        else:
            a = c_new
        c_old = c_new
        c_new = (a*func(b)-b*func(a))/(func(b)-func(a))

    print("[{}]ANS: {}".format(func.__name__, c_new))
    print("-----------------------------------")


if __name__ == "__main__":
    sol(f1, -2, 2)
    sol(f2, -5, 5)
    sol(f3, -4, 3)
    sol(f4, -6, 2)
