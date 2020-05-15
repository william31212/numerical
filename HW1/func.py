import math

def test(x):
    return x*x*x + 2*x - 3

# a: -2, b: +2
def f1(x):
    return math.exp(x)-3*x*math.cos(2*x)-8.3

# a:-5, b: +5
def f2(x):
    return math.exp(x*math.sin(x))-x*math.cos(2*x)-2.8

# a: -4, b: +3
def f3(x):
    return 4*math.exp(x*math.sin(x)*math.cos(x))-10

# a: -6, b: +2
def f4(x):
    return math.sin(3*x)-x*math.cos(x)-math.exp(x)+3.8

def f1_deri(x):
    return math.exp(x)-3*(-2*x*math.sin(2*x)+math.cos(2*x))

def f2_deri(x):
    return math.exp(x*math.sin(x))*x*math.cos(x)+math.exp(x*math.sin(x))*math.sin(x)+2*x*math.sin(2*x)-math.cos(2*x)

def f3_deri(x):
    return 4*math.exp(x*math.sin(2*x))*(x*math.cos(2*x)+(1/2)*math.sin(2*x))

def f4_deri(x):
    return 3*math.cos(3*x)-math.exp(x)+x*math.sin(x)-math.cos(x)


def f1_fixed(x):
    return math.log(3*x*math.cos(2*x))+8.3

def f2_fixed(x):
    return math.log(x*math.cos(2*x)+2.8)/math.sin(x)

def f3_fixed(x):
    return math.log(2.5)/math.sin(x)*math.cos(x)

def f4_fixed(x):
    return math.log(3.8-x*math.cos(x)+math.sin(3*x))

def show_message(name, cnt, a, c, b):
    print("[{}]step {}: a:{} b:{} c:{}".format(name, cnt, a, c, b))
