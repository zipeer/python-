# 1.输入苹果的单价
price_str = input("苹果的单价：")
# 2.输入重量
weight_str = input("苹果的重量：")
# 3.输入总金额
price = float(price_str)
weight = float(weight_str)


money = price * weight
print("苹果的总金额为：")
print(money)