import math
from func import *

# Newten'sMethod
# deviation
e = 10e-10

def sol(func, func_deri):
    x = 3.2
    cnt = 0
    delta = func(x)/func_deri(x)
    x = x - delta
    print("[{}]step {} x:{} delta:{}".format(func.__name__, cnt, x, delta))
    while abs(delta) >= e:
        cnt += 1
        delta = func(x)/func_deri(x)
        x = x - delta
        print("[{}]step {} x:{} delta:{}".format(func.__name__, cnt, x, delta))

    print("[{}]ANS: {}".format(func.__name__, x))
    print("-----------------------------------")

if __name__ == "__main__":
    sol(f1, f1_deri)
    sol(f2, f2_deri)
    sol(f3, f3_deri)
    sol(f4, f4_deri)
