def demo(num,*nums,**person):
    """
    
    :param num: 单值变量
    :param nums: 元组
    :param person: 字典
    :return: 
    """
    print(num)
    print(nums)
    print(person)

# demo(1)
demo(1,2,3,4,5,name="小明",age=18)