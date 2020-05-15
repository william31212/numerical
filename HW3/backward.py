import numpy as np
import matplotlib.pyplot as plt
import random
from data import *

y = [[0 for i in range(25)]
        for j in range(25)]

def fact(n):
    f = 1
    for i in range(2, n+1):
        f *= i
    return f

def backward_init(x, f_x):
    for i in range(len(f_x)):
        y[i][0] = f_x[i]

    for i in range(1,len(x)):
        for j in range(len(x)-1, i-1, -1):
            y[j][i] = y[j][i-1] - y[j-1][i-1]


def backward_method(input_x, x):
    sum = y[len(x)-1][0]
    s = (input_x - x[len(x)-1])/ (x[1] - x[0])
    for i in range(1, len(x)):
        tmp = s
        for j in range(1, i):
            tmp = tmp * (s+j)
        sum += tmp * y[len(x)-1][i] / fact(i)
    return sum


backward_x = []
backward_y = []
lag_i = 0.0001


def clear_backward():
    backward_x.clear()
    backward_y.clear()


def gen_backward(x):
    i = a
    while i < b:
        backward_x.append(i)
        backward_y.append(backward_method(i, x))
        i += lag_i
    backward_x.append(b)
    backward_y.append(backward_method(i, x))


def main():
    plt.figure()
    # plt.suptitle('backward', fontsize=10)
    backward_init(x_same, f_x_same)
    gen_backward(x_same)
    # plt.subplot(1, 1, 2)
    plt.title('backward', fontsize=10)
    plt.scatter(backward_x, backward_y, s=5)
    plt.scatter(x_same, f_x_same, s=5)
    clear_data()
    plt.show()

if __name__ == "__main__":
    main()
