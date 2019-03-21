# 全局变量
num1 = 10

def demo1():

    # 希望修改全局变量的值，使用global声明一下即可
    global num1
    num1 = 99
    # 局部变量
    print("%d" %num1)
    # 输出结果没发生变化

def demo2():
    print("%d" % num1)
    # 如果内部没有找到局部变量，就向外找全局变量

demo1()
demo2()