import math
from func import *

# Bisection-Method
# deviation
e = 10e-10

def sol(func, a, b):
	global e
	m = 0
	cnt = 0

	if func(a) * func(b) > 0:
		print("[X]{} Cannot solve, because f(a) * f(b) > 0".format(func.__name__))
		print("-----------------------------------")
		return False

	while abs(b-a) > e:
		m = (a+b)/2
		show_message(func.__name__, cnt, a, m, b)
		if func(a) * func(m) < 0:
			b = m
		else:
			a = m
		cnt += 1
	print("[{}]ANS: {}".format(func.__name__, m))
	print("-----------------------------------")

if __name__ == "__main__":
	sol(f1, -2, 2)
	sol(f2, -5, 5)
	sol(f3, -4, 3)
	sol(f4, -6, 6)
