a = 6
b = 100

# 解法一：使用其他变量
c = a
a = b
b = c

# 解法二：不适用其他变量
a = a + b
b = a - b
a = a - b

# 解法三：python专用

# 等号后面是元组，小括号省略
a,b = b,a

print(a)
print(b)