name = "小明"
# say_hello()不能在定义之前调用
# F7 step into debug函数
# CTRL+Q 查看函数的说明

def say_hello():
    """
    打招呼 
    """
    print("hello 1")
    print("hello 2")
    print("hello 3")

    print(name)
# 只有在程序中主动调用才会执行函数
print(name)
say_hello()
print(name)