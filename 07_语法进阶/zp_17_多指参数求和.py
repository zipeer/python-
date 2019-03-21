def sum_numbers(*args):
# def sum_numbers(args):
    """多指参数调用比较简单
    
:param args: 
:return: 
"""
    num = 0
    print(args)
    # 循环遍历
    for n in args:
        num += n

    return num

result = sum_numbers(1,2,3,4,5)
print(result)