# 定义一个函数 sum-number
# 能够接收一个num的整数参数
# 计算结果

def sum_numbers(num):
    # 出口
    if num == 1:
        return 1

    # 数字的累加
    # 假设sum_number()能够处理累加
    temp = sum_numbers(num - 1)

    return num + temp

result = sum_numbers(100)
print(result)