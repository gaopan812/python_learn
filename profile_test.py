import time


def fun1():
    print('fun2')
    time.sleep(1)


def fun2():
    print('fun3')
    time.sleep(2)


def fun3():
    print('fun5')
    time.sleep(1)
    fun2()


fun1()
fun2()
fun3()