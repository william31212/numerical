import numpy as np
import matplotlib.pyplot as plt
import random
from data import *

a = 2.5
b = 7.5

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
lag_i = 0.0001


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


def main():
    plt.figure()
    plt.suptitle('newton', fontsize=10)
    newton_init(x_diff, f_x_diff)
    gen_newton(x_diff)
    plt.subplot(1, 2, 1)
    plt.title('testcase 1', fontsize=10)
    plt.scatter(newton_x, newton_y, s=5)
    plt.scatter(x_diff, f_x_diff, s=5)
    clear_data()

    newton_init(x_same, f_x_same)
    gen_newton(x_same)
    plt.subplot(1, 2, 2)
    plt.title('testcase 2', fontsize=10)
    plt.scatter(newton_x, newton_y, s=5)
    plt.scatter(x_same, f_x_same, s=5)
    clear_data()
    plt.show()


if __name__ == "__main__":
    main()
