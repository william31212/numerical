import numpy as np
import matplotlib.pyplot as plt
import random
from data import *

def lagrange(xp, x, f_x):
    yp = 0
    for i in range(0, len(x)):
        p = 1
        for j in range(0, len(x)):
            if i != j:
                p *= (xp - x[j])/(x[i] - x[j])
        yp += p * f_x[i]
    return yp


lag_x = []
lag_y =[]
lag_i = 0.0001

def gen_lagrange(x, f_x):
    i = a
    while i < b:
        lag_x.append(i)
        lag_y.append(lagrange(i, x, f_x))
        i += lag_i
    lag_x.append(b)
    lag_y.append(lagrange(b, x, f_x))


def clear_lagrange():
    lag_x.clear()
    lag_y.clear()
