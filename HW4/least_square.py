import numpy as np
import matplotlib.pyplot as plt
import math
import sys

x_data = [0.00, 0.20, 0.48, 0.61, 0.80, 1.01, 1.12, 1.27, 1.48, 1.72, 1.97, 2.25, 2.52, 2.78, 2.94, 3.25, 3.39, 3.71, 4.02, 4.13, 4.24, 4.33,
		  4.64, 4.87, 5.06, 5.17, 5.44, 5.53, 5.77, 5.88, 6.19, 6.42, 6.70, 6.91, 7.17, 7.34, 7.49, 7.60, 7.92, 8.15, 8.41, 8.61, 8.73, 9.00, 9.20]

y_data = [1.0000, 1.2482, 1.7019, 1.8899, 2.0800, 2.1157, 2.0514, 1.8839, 1.5201, 1.0361, 0.6630, 0.5458, 0.7697, 1.1515, 1.4096, 1.7564, 1.8162, 1.7406, 1.5357, 1.4631, 1.4105, 1.3752,
		  1.3337, 1.3300, 1.3022, 1.2625, 1.1111, 1.0496, 0.8930, 0.8547, 0.9213, 1.1665, 1.5988, 1.9059, 2.1186, 2.0953, 1.9652, 1.8140, 1.1951, 0.7906, 0.5518, 0.5768, 0.6775, 1.0472, 1.3796]

def find_matrix(dim):
	arr = np.array([])
	# find A
	cnt = 0
	for i in range(1, dim+1):
		if i == 1:
			for j in range(0, dim):
				if j == 0:
					arr = np.append(arr, len(x_data))
				else:
					tmp = 0
					for x in x_data:
						tmp += pow(x, j)
					arr = np.append(arr, tmp)
		else:
			tmp_arr = arr[-(dim-1):]
			back_tmp = 0

			for x in x_data:
				back_tmp += pow(x, dim+cnt)
			cnt += 1

			tmp_arr = np.append(tmp_arr, back_tmp)
			arr = np.append(arr, tmp_arr)
	arr = np.reshape(arr, (dim,dim))

	# find b
	b = np.array([])
	for i in range(0, dim):
		tmp = 0
		for idx in range(len(x_data)):
			tmp += y_data[idx] * pow(x_data[idx], i)
		b = np.append(b, tmp)

	return arr, b

def solve(A, b):
	x = np.linalg.solve(A, b)
	return x

def cal_least_y(x):
	least_y = []

	for i in range(len(x_data)):
		tmp = 0
		for j in range(len(x)):
			tmp += x[j] * pow(x_data[i], j)
		least_y.append(tmp)

	return least_y

def cal_delta(src, aft, dim):
	delta = 0
	for i in range(0, len(src)):
		delta += pow(aft[i] - src[i], 2)

	tmp = len(src) - dim
	if tmp == 0:
		return sys.float_info.max
	else:
		delta /= tmp
	return math.sqrt(delta)

def find_best_choice(error):
	best = 0
	best_val = sys.float_info.max
	for i in range(len(error)):
		if error[i] <= best_val:
			best_val = error[i]
			best = i+2
	return best

def main():
	error = []
	f = open('f(x).txt', 'w')
	error_txt = open('error.txt', 'w')

	f.write("x    f(x)\n")
	for idx in range(len(x_data)):
			f.write(str(x_data[idx]) + " " +  str(y_data[idx]) + '\n')

	error_txt.write("x    p(x)\n")

	for i in range(2, 46):
		plt.figure()
		A, b = find_matrix(i)
		x = solve(A, b)
		least_y = cal_least_y(x)
		delta = cal_delta(y_data, least_y, i)
		error.append(delta)
		error_txt.write("{}    {:.6f}\n".format(i, delta))

		# plt.title('Least square => P' + str(i) +'(x)', fontsize=10)
		# plt.scatter(x_data, y_data, s=5)
		# plt.plot(x_data, y_data, label='f(x)')

		# plt.scatter(x_data, least_y, s=5, color='red')
		# plt.plot(x_data, least_y, color='red', label='P(x)')
		# plt.legend(loc='upper right')

		# plt.savefig("./result/P" + str(i) + "(x).png", dpi=300)

	tmp = find_best_choice(error)
	print("The best choice is {}".format(tmp))

if __name__ == '__main__':
	main()