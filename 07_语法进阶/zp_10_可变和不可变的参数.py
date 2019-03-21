def demo(num):

    print("函数内部的代码")
    # 在函数内部，不会修改外部的实参变量
    # 修改只能在函数内部生效
    num = 100
    num_list = [1,2,3]
    """
    247
    """
    print(num)
    print(num_list)
    print("函数执行完成")

gl_num = 99
gl_list = [4,5,6]
demo(gl_num)

print(gl_num)
print(gl_list)