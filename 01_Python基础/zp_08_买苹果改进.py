# 1.提示用户输入苹果的单价
price = float(input("苹果的单价："))
# 2.提示输入重量
weight = float(input("苹果的重量："))
# 3.计算金额
money = price * weight
print(money)

print("=======================")
print("请输入任意一个整数：")
number = int(input())
if number == 10:
    print("你输入的数字时：%d"%number)
    print("你猜对了！")
else:
    print("你猜错了！")
