def demo1():

    # 定义一个局部变量
    # 变量周期
    # 1>出生：执行下方代码之后，才会被创建
    # 2>死亡：函数执行之后
    num = 10
    print("demo1函数内部的变量是%d" % num)

def demo2():
    num = 99
    print("demo2 ==> %d" % num)

    pass

# print("%d" % num)
demo1()
demo2()