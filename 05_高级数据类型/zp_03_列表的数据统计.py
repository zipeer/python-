name_list = ["张三","李四","王五","王小二","张三"]

# 统计列表中元素的个数
list_len = len(name_list)
print("列表中有%d个元素"%list_len)

# 统计指定数据出现的次数
count = name_list.count("张三")
print("张三出现了%d次"%count)

name_list.remove("张三")
print(name_list)