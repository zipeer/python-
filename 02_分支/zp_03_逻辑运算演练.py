# 练习1: 定义一个整数变量 age，编写代码判断年龄是否正确
# 要求人的年龄在 0-120 之间
age = int(input("你的年龄是多少？"))
if age >= 0 and age <= 120:
    print("年龄正确！")
else:
    print("年龄不正确！")

# 练习2: 定义两个整数变量 python_score、c_score，编写代码判断成绩
# 要求只要有一门成绩 > 60 分就算合格
python_score = int(input("python的成绩"))
c_score = int(input("c的成绩"))

# 练习3: 定义一个布尔型变量 is_employee，编写代码判断是否是本公司员工
# 如果不是提示不允许入内
is_employee = bool(input("是否是本公司员工?"))
