info_tuple = ("小明",18,175)

# 格式化字符串后面的（）本质上是元组
print("%s的年龄是%d,身高是%.2f"%info_tuple)

# 可以拼接成新的字符串
info_str = "%s的年龄是%d,身高是%.2f"%info_tuple
print(info_str)