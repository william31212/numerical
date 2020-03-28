import math
from func import *

# Secant-Method
# deviation

e = 10e-10

def sol(func, a, b):
    c = ((a*func(b))-(b*func(a)))/(func(b)-func(a))
    a = b
    b = c
    cnt = 0
    print("[{}]step {} a:{} b:{} c:{}".format(func.__name__, cnt, a, c, b))
    while abs(b-a) >= e:
        if func(b)-func(a) == 0:
            print("[X]{} Cannot solve, float division by zero".format(func.__name__))
            print("-----------------------------------")
            return False
        cnt += 1
        c = ((a*func(b))-(b*func(a)))/(func(b)-func(a))
        print("[{}]step {} a:{} b:{} c:{}".format(func.__name__, cnt, a, c, b))
        a = b
        b = c

    print("[{}]ANS: {}".format(func.__name__, b))
    print("-----------------------------------")



if __name__ == "__main__":
    sol(f1, -2, 2)
    sol(f2, -5, 5)
    sol(f3, -4, 3)
    sol(f4, -6, 10)
