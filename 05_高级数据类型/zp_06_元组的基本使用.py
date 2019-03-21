# 元组的数据不可修改，保护数据安全
info_tuple = ("zhangsan",18,175,18)


# 和列表基本相同
# 1,取值和取索引
print(info_tuple[0])
print(info_tuple.index("zhangsan"))

# 2，统计计数

print(info_tuple.count(18))
# 统计元素个数
print(len(info_tuple))