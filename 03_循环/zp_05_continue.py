# 在循环过程中，如果 某一个条件满足后，不 希望 执行循环代码，但是又不希望退出循环，可以使用 continue
i = 0
while i < 10:
    if i == 3:
        i += 1
        continue# 不加处理语句会死循环，
    print(i)
    i += 1
print("over!")
# continue直接返回while