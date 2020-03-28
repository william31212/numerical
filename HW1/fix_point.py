import math
from func import *

# Fixed-point-Method
# deviation
e = 10e-10

def sol(func):
    x_old = -2.0
    cnt = 0
    x_new = func(x_old)

    print("[{}]step {}: x_old:{} x_new:{}".format(func.__name__, cnt, x_old, x_new))
    while abs(x_new - x_old) >= e:
        cnt += 1
        x_old = x_new
        x_new = func(x_old)
        print("[{}]step {}: x_old:{} x_new:{}".format(func.__name__, cnt, x_old, x_new))

    print("[{}]ANS: {}".format(func.__name__, x_new))
    print("-----------------------------------")


if __name__ == "__main__":
    # sol(f1_fixed)
    sol(f2_fixed)
    # sol(f3_fixed)
    sol(f4_fixed)
