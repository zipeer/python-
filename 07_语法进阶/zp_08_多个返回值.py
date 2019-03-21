def measure():

    # 测量温度 湿度
    print("测量开始...")
    temp = 39
    wetness = 50
    print("测量结束")

    # 元组返回对各值
    # 如果返回的值是元组，小括号可以省略
    return  temp,wetness

# 元组
result = measure()
print(result)

# 需求：单独拿出温度或者湿度--不方便
print(result[0])
print(result[1])

# 获得元组中单个元素时，可以使用多个变量，依次接收返回结果
gl_temp,gl_wetness = measure()

print(gl_temp)
print(gl_wetness)