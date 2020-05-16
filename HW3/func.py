import math
from lagrange import *
from newton import *
from forward import *
from backward import *


def func_1(x):
    return math.exp(x*math.sin(x))-x*math.cos(2*x)-2.8

