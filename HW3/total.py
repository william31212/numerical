import random
from lagrange import *
from newton import *
from forward import *
from backward import *
from data import *
from func import *


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
    plt.plot(lag_x, lag_y, label='P(x)')
    plt.plot(x_diff, f_x_diff, label='y(x)')
    plt.legend(loc='best')
    # newton
    plt.subplot(1, 2, 2)
    plt.title('newton', fontsize=10)
    newton_init(x_diff, f_x_diff)
    gen_newton(x_diff)
    plt.plot(newton_x, newton_y, label='P(x)')
    plt.plot(x_diff, f_x_diff, label='y(x)')
    plt.legend(loc='best')
    plt.savefig("./result/testcase1.png",dpi=300)


def testcase2():
    plt.figure()
    # testcase1
    plt.suptitle('testcase2-same', fontsize=10)
    # lagrange
    plt.subplot(2, 2, 1)
    plt.title('lagrange', fontsize=10)
    gen_lagrange(x_same, f_x_same)
    plt.plot(lag_x, lag_y, label='P(x)')
    plt.plot(x_same, f_x_same, label='y(x)')
    plt.legend(loc='best')
    # newton
    plt.subplot(2, 2, 2)
    plt.title('newton', fontsize=10)
    newton_init(x_same, f_x_same)
    gen_newton(x_same)
    plt.plot(newton_x, newton_y, label='P(x)')
    plt.plot(x_same, f_x_same, label='y(x)')
    plt.legend(loc='best')
    # forward
    plt.subplot(2, 2, 3)
    plt.title('forward', fontsize=10)
    forward_init(x_same, f_x_same)
    gen_forward(x_same)
    plt.plot(forward_x, forward_y, label='P(x)')
    plt.plot(x_same, f_x_same, label='y(x)')
    plt.legend(loc='best')
    # backward
    plt.subplot(2, 2, 4)
    plt.title('backward', fontsize=10)
    backward_init(x_same, f_x_same)
    gen_backward(x_same)
    plt.plot(backward_x, backward_y, label='P(x)')
    plt.plot(x_same, f_x_same, label='y(x)')
    plt.legend(loc='best')
    plt.savefig("./result/testcase2.png", dpi=300)

# 畫函數圖
def my_func_result():
    i = a
    while i < b:
        x_func.append(i)
        f_x_func.append(func_1(i))
        i += lag_i
    x_func.append(b)
    f_x_func.append(func_1(b))

    plt.plot(x_func, f_x_func, label='function')
    plt.legend(loc='best')
    plt.savefig("./result/func.png", dpi=300)



# 用取的點數量做比較(12, 15, 18, 20)，區間2.5 ~ 7.5之間
def gen_interval():
    tmp_range= (b-a)/12
    i = a
    while i < b:
        x_12_interval.append(i)
        f_x_12_interval.append(func_1(i))
        i += tmp_range
    x_12_interval.append(b)
    f_x_12_interval.append(func_1(b))

    tmp_range = (b-a)/15
    i = a
    while i < b:
        x_15_interval.append(i)
        f_x_15_interval.append(func_1(i))
        i += tmp_range
    x_15_interval.append(b)
    f_x_15_interval.append(func_1(b))


    tmp_range = (b-a)/18
    i = a
    while i < b:
        x_18_interval.append(i)
        f_x_18_interval.append(func_1(i))
        i += tmp_range
    x_18_interval.append(b)
    f_x_18_interval.append(func_1(b))

    tmp_range = (b-a)/20
    i = a
    while i < b:
        x_20_interval.append(i)
        f_x_20_interval.append(func_1(i))
        i += tmp_range
    x_20_interval.append(b)
    f_x_20_interval.append(func_1(b))

interval = [12, 15, 18, 20]
x_func_testcase = [x_12_interval, x_15_interval, x_18_interval, x_20_interval]
f_x_func_testcase = [f_x_12_interval, f_x_15_interval, f_x_18_interval, f_x_20_interval]

def testcase3():
    global x_interval, f_x_interval

    # lagrange
    cnt = 1
    plt.figure()
    for i in range(len(interval)):
        plt.subplot(2, 2, cnt)
        plt.title('interval: '+ str(interval[i]), fontsize=10)
        gen_lagrange(x_func_testcase[i], f_x_func_testcase[i])
        plt.plot(x_func_testcase[i], f_x_func_testcase[i], label='P(x)')
        plt.plot(x_func, f_x_func, label='y(x)')
        plt.legend(loc='best')
        cnt += 1
    plt.savefig("./result/lagrange_diff.png", dpi=300)

    # newton
    cnt = 1
    plt.figure()
    for i in range(len(interval)):
        plt.subplot(2, 2, cnt)
        plt.title('interval: ' + str(interval[i]), fontsize=10)
        newton_init(x_func_testcase[i], f_x_func_testcase[i])
        gen_newton(x_func_testcase[i])
        plt.plot(x_func_testcase[i], f_x_func_testcase[i], label='P(x)')
        plt.plot(x_func, f_x_func, label='y(x)')
        plt.legend(loc='best')
        cnt += 1
    plt.savefig("./result/newton_diff.png", dpi=300)

    # forward
    cnt = 1
    plt.figure()
    for i in range(len(interval)):
        plt.subplot(2, 2, cnt)
        plt.title('interval: ' + str(interval[i]), fontsize=10)
        forward_init(x_func_testcase[i], f_x_func_testcase[i])
        gen_forward(x_func_testcase[i])
        plt.plot(x_func_testcase[i], f_x_func_testcase[i], label='P(x)')
        plt.plot(x_func, f_x_func, label='y(x)')
        plt.legend(loc='best')
        cnt += 1
    plt.savefig("./result/forward_diff.png", dpi=300)

    # backward
    cnt = 1
    plt.figure()
    for i in range(len(interval)):
        plt.subplot(2, 2, cnt)
        plt.title('interval: ' + str(interval[i]), fontsize=10)
        backward_init(x_func_testcase[i], f_x_func_testcase[i])
        gen_forward(x_func_testcase[i])
        plt.plot(x_func_testcase[i], f_x_func_testcase[i], label='P(x)')
        plt.plot(x_func, f_x_func, label='y(x)')
        plt.legend(loc='best')
        cnt += 1
    plt.savefig("./result/backward_diff.png", dpi=300)







def main():
    # testcase1()
    # clear_data()
    # testcase2()
    # clear_data()
    my_func_result()
    gen_interval()
    testcase3()

if __name__ == "__main__":
    main()
