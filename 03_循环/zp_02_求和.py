# 计算 0 ~ 100 之间所有数字的累计求和结果
# 1.定义一个变量记录循环次序,定义一个最终结果
result = 0
i = 0
# 2.开始循环
while i <= 100:
    result += i# result = result + i
    # 处理计数器
    i += 1
print("0~100的和为：%d"%result)