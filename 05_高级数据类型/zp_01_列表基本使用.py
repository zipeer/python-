# 列表的数据可以修改
name_list = ["zhangsan","lisi","wangwu"]

# 1.取值和取索引
# 如果内容不在，超出范围，提示错误
print(name_list[2])
print(name_list.index("wangwu"))

# 2.修改
name_list[1] = "李四"
#name_list[3] = "小明"
# list assignment index out of range
# 列表指定的位置超出范围，报错

# 3.增加
name_list.append("王小二")
# append方法可以在列表的末尾增加数据

name_list.insert(1,"小明")
# insert 指定位置和数据

temp_list = ["孙笑怡","二师弟","三师弟"]
name_list.extend(temp_list)
# extend 可以在末尾将其他列表的内容增加

# 4.删除
# remove方法直接删除指定数据
name_list.remove("wangwu")

# pop方法默认删除最后一个数据
name_list.pop()
# pop方法可指定位置删除
name_list.pop(3)

# clear方法删除所有数据
name_list.clear()


print(name_list)