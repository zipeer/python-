def test(num):

    print("在函数内部%d 对应的内存地址是%d"%(num,id(num)))

    # 1> 定义一个字符串变量
    result = "hello"
    print("函数要返回数据的内存地址是 %d" % id(result))

    # 2> 将字符串变量返回
    return result

# 定义一个数字变量
a = 10

print("a 变量保存数据的内存地址是 %d" % id(a))

# 调用test函数,传递的是地址，不是数值

# r,result为hello的标签
r = test(a)

print("%s的内存地址是%d"%(r,id(r)))