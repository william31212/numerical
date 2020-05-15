import numpy as np
import matplotlib.pyplot as plt
import random
from data import *

a = 2.5
b = 7.5

y = [[0 for i in range(25)]
        for j in range(25)]

def fact(n):
    f = 1
    for i in range(2, n+1):
        f *= i
    return f

def forward_init(x, f_x):
    for i in range(len(f_x)):
        y[i][0] = f_x[i]

    for i in range(1,len(x)):
        for j in range(len(x)-i):
            y[j][i] = y[j+1][i-1] - y[j][i-1]


def forward_method(input_x, x):
    sum = y[0][0]
    s = (input_x - x[0])/ (x[1] - x[0])
    for i in range(1, len(x)):
        tmp = s
        for j in range(1, i):
            tmp = tmp * (s-j)
        sum += tmp * y[0][i] / fact(i)
    return sum


forward_x = []
forward_y = []

def clear_forward():
    forward_x.clear()
    forward_y.clear()


def gen_forward(x):
    i = a
    while i < b:
        forward_x.append(i)
        forward_y.append(forward_method(i, x))
        i += lag_i
    forward_x.append(b)
    forward_y.append(forward_method(i, x))


def main():
    plt.figure()
    # plt.suptitle('forward', fontsize=10)
    forward_init(x_same, f_x_same)
    # plt.subplot(1, 1, 2)
    plt.title('forward', fontsize=10)
    gen_forward(x_same)
    plt.scatter(forward_x, forward_y, s=5)
    plt.scatter(x_same, f_x_same, s=5)
    clear_data()
    plt.show()

if __name__ == "__main__":
    main()
