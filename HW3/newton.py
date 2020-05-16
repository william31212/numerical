import numpy as np
import matplotlib.pyplot as plt
import random
from data import *


y = [[0 for i in range(25)]
     for j in range(25)]

# 先build表
def newton_init(x, f_x):
    for i in range(len(f_x)):
        y[i][0] = f_x[i]
    for i in range(1, len(x)):
        for j in range(len(x) - i):
            y[j][i] = ((y[j][i - 1] - y[j + 1][i - 1]) / (x[j] - x[i + j]))

# 計算
def newton_method(input_x, x):
    sum = y[0][0]
    for i in range(1, len(x)):
        pro = 1
        for j in range(i):
            pro = pro * (input_x - x[j])
        sum += pro * y[0][i]
    return sum


newton_x = []
newton_y = []


def gen_newton(x):
    i = a
    while i < b:
        newton_x.append(i)
        newton_y.append(newton_method(i, x))
        i += lag_i
    newton_x.append(b)
    newton_y.append(newton_method(i, x))


def clear_newton():
    newton_x.clear()
    newton_y.clear()


