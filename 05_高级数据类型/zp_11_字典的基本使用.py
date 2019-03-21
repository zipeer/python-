xiaoming_dict = {"name":"小明"}

# 1,取值
print(xiaoming_dict["name"])

# 2.增加/修改
# key不存在，增加
xiaoming_dict["age"] = 18
# key存在，修改
xiaoming_dict["name"] = "小小明"

# 3.删除
# 删除指定的key对应的数据
xiaoming_dict.pop("age")
# xiaoming_dict.pop("age123")

print(xiaoming_dict)