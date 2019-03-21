def sum_number(num):

    print(num)
    # 递归出口，当参数满足魔偶个条件时，不再执行函数
    # 没有出口，陷入死循环
    if num == 0:
        return

    # 自己调用自己
    sum_number(num - 1)

sum_number(3)