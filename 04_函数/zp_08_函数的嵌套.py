# 一个函数里面 又调用 了 另外一个函数，这就是 函数嵌套调用
# 如果函数 test2 中，调用了另外一个函数 test1
# 那么执行到调用 test1 函数时，会先把函数 test1 中的任务都执行完
# 才会回到 test2 中调用函数 test1 的位置，继续执行后续的代码
def test1():
    print("*"*50)
    print("test1")
    print("*"*50)
def test2():
    print("-"*50)
    test1()
    print("+"*50)

test2()