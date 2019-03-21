def print_info(name,gender=True):
    """
    
    :param name: 班上同学的姓名
    :param gender: True 男生  False 女生
    :return: 
    """

    gender_text = "男生"

    if not gender:
        gender_text = "女生"

    print("%s是%s"% (name,gender_text))
# 在指定缺省参数时，应指定最常见的值
print_info("小明")
print_info("老王")
print_info("小美",False)