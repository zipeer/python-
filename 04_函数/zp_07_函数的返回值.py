# 在程序开发中，有时候，会希望 一个函数执行结束后，告诉调用者一个结果，以便调用者针对具体的结果做后续的处理
# 返回值 是函数 完成工作后，最后 给调用者的 一个结果
# 在函数中使用 return 关键字可以返回结果
# 调用函数一方，可以 使用变量 来 接收 函数的返回结果
def sum_2_num(num1,num2):
    result = num1 + num2
    return result
    # print("*")# 这一行的代码不会执行

result = sum_2_num(10,20)
print("计算的结果为：%d"%result)