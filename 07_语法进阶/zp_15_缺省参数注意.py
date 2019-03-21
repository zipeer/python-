def print_info(name,title="学生", gender=True):
    """

    :param title: 职位
    :param name: 班上同学的姓名
    :param gender: True 男生  False 女生
    :return: 
    """

    # 缺省参数应放在参数定义的末尾
    gender_text = "男生"

    if not gender:
        gender_text = "女生"

    print("[%s]%s是%s" % (title,name, gender_text))


# 在指定缺省参数时，应指定最常见的值
print_info("小明")
print_info("老王")
print_info("小美", gender=False)