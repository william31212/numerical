from lagrange import *
from newton import *
from forward import *
from backward import *

def clear_data():
    clear_lagrange()
    clear_newton()
    clear_forward()
    clear_backward()


def testcase1():
    plt.figure()
    # testcase1
    plt.suptitle('testcase1-diff', fontsize=10)
    # lagrange
    plt.subplot(1, 2, 1)
    plt.title('lagrange', fontsize=10)
    gen_lagrange(x_diff, f_x_diff)
    plt.scatter(lag_x, lag_y, s=5)
    plt.scatter(x_diff, f_x_diff, s=5)
    # newton
    plt.subplot(1, 2, 2)
    plt.title('newton', fontsize=10)
    newton_init(x_diff, f_x_diff)
    gen_newton(x_diff)
    plt.scatter(newton_x, newton_y, s=5)
    plt.scatter(x_diff, f_x_diff, s=5)
    plt.show()


def testcase2():
    plt.figure()
    # testcase1
    plt.suptitle('testcase2-same', fontsize=10)
    # lagrange
    plt.subplot(2, 2, 1)
    plt.title('lagrange', fontsize=10)
    gen_lagrange(x_same, f_x_same)
    plt.scatter(lag_x, lag_y, s=5)
    plt.scatter(x_same, f_x_same, s=5)
    # newton
    plt.subplot(2, 2, 2)
    plt.title('newton', fontsize=10)
    newton_init(x_same, f_x_same)
    gen_newton(x_same)
    plt.scatter(newton_x, newton_y, s=5)
    plt.scatter(x_same, f_x_same, s=5)
    # forward
    plt.subplot(2, 2, 3)
    plt.title('forward', fontsize=10)
    forward_init(x_same, f_x_same)
    gen_forward(x_same)
    plt.scatter(forward_x, forward_y, s=5)
    plt.scatter(x_same, f_x_same, s=5)
    # backward
    plt.subplot(2, 2, 4)
    plt.title('backward', fontsize=10)
    backward_init(x_same, f_x_same)
    gen_backward(x_same)
    plt.scatter(backward_x, backward_y, s=5)
    plt.scatter(x_same, f_x_same, s=5)
    plt.show()

def main():
    testcase1()
    clear_data()
    testcase2()
    clear_data()

if __name__ == "__main__":
    main()
