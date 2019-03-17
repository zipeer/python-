import  cards_tools
while True:

    # TODO(张朋) 显示功能菜单(解决后删除)
    # 在主函数中直接写比较繁琐，使用函数
    cards_tools.show_menu()

    action_str = input("请选择希望执行的操作：")
    print("你选择的操作是：【%s】"%action_str)

    # 123针对名片操作
    if action_str in ["1","2","3"]:

        # 新增名片
        if action_str == "1":
            cards_tools.new_card()
        # 显示全部
        elif action_str == "2":
            cards_tools.show_all()
        elif action_str == "3":
            cards_tools.search_card()

        pass
    # 0退出系统
    elif action_str == "0":

        print("欢迎在此使用【名片管理系统】")

        break
        # 表示一个占位符，能够保证程序正确，不会执行任何操作
        # pass 如果不确定怎么写代码，就先用pass占位


    # 其他提示输入错误
    else:
        print("你输入的不正确，请重新输入")