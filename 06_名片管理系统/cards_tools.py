# 记录所有的名片字典
card_list =[]

def show_menu():

    """显示菜单"""
    print("*"*50)
    print("欢迎使用【名片管理系统】")
    print("")
    print("1.新增名片")
    print("2.显示全部")
    print("3.搜索名片")
    print("")
    print("0.推出系统")
    print("*"*50)

def new_card():

    """新增名片"""
    print("-" * 50)
    print("新增名片")

    # 提示输入信息
    name_str = input("请输入姓名：")
    phone_str = input("电话")
    qq_str = input("QQ")
    email_str = input("邮箱")

    # 使用信息建立字典
    card_dict = {"name":name_str,
                 "phone":phone_str,
                 "qq":qq_str,
                 "email":email_str}

    # 将名片字典添加到列表
    card_list.append(card_dict)

    print(card_list)

    # 提示成功
    print("添加成功")


def show_all():

    """显示所有名片"""
    print("显示所有名片")
    print("-" * 50)

    # 判断是否存在记录
    if len(card_list) == 0:
        print("没有任何记录")

        # 可以返回函数的执行结果
        # return 下方的代码不执行
        # 不加任何内容，就返回到调用函数的位置
        return

    # 打印表头
    for name in ["姓名","电话","QQ","邮箱"]:
        print(name,end="\t\t")

    print("")

    # 打印分割线
    print("="*50)

    # 遍历所有信息
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                       card_dict["phone"],
                                       card_dict["qq"],
                                       card_dict["email"]))

def search_card():

    """搜索名片"""
    print("-" * 50)
    print("搜索名片")

    # 提示要搜索的内容
    find_name = input("请输入要搜索的姓名：")
    # 遍历列表
    for card_dict in card_list:
        if card_dict["name"] == find_name:
            print("姓名\t\t电话\t\tQQ\t\t邮箱")
            print("="*50)
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                            card_dict["phone"],
                                            card_dict["qq"],
                                            card_dict["email"]))
            #  针对找到的名片执行删除和修改的操作
            deal_card(card_dict)

            break
    else:
        print("没有找到%s" % find_name)

def deal_card(find_dict):
    """处理查找到的名片

    :param find_dict: 查找到的名片
    """
    print(find_dict)

    action_str = input("请选择要执行的操作："
                       "【1】 修改 【2】 删除 【0】 返回上级菜单")
    # 修改
    if action_str == "1":
        find_dict["name"] = input_card_info(find_dict["name"],"姓名：[回车不修改]")
        find_dict["phone"] = input_card_info(find_dict["phone"],"电话：[回车不修改]")
        find_dict["qq"] = input_card_info(find_dict["qq"],"QQ:[回车不修改]")
        find_dict["email"] = input_card_info(find_dict["email"],"邮箱：[回车不修改]")
        print("已经修改名片")
    # 删除
    elif action_str == "2":
        card_list.remove(find_dict)
        print("已经删除名片")


def input_card_info(dict_value,tip_message):
    # 提示输入内容
    """输入名片信息
    
    :param dict_value: 字典中原有的值
    :param tip_message: 输入提示的文字
    :return: 如果输入内容，就返回内容，否则返回字典中原有的值
    """
    result_str = input(tip_message)
    # 对内容进行判断，如果输入了，直接返会结果
    if len(result_str) > 0:
        return result_str
    # 如果没有输入，返回原有的值
    else:
        return dict_value
    pass
