# 定义字符串变量，name，输出
name = "大明"
print("我的名字叫%s，请多多关照！"%name)
# 定义学号,输出0001
student_no = 1
print("我的学号是%04d"%student_no)# 如果不满4位，补0

price = 8.5
weight = 7.5
money = price * weight
# 控制小数的位数
print("苹果的单价是%.2f，购买了%.3f斤，总金额是%.4f元。"%(price,weight,money))

# 定义一个小数 scale，输出 数据比例是 10.00%
scale = 0.25
print("数据比例是：%.2f%%"%(scale*100))