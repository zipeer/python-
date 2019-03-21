# 1> 完成 5 行内容的简单输出
# 2> 分析每行内部的 * 应该如何处理？
    # 每行显示的星星和当前所在的行数是一致的
    # 嵌套一个小的循环，专门处理每一行中 列 的星星显示

row = 1
lie = 1
while row <= 5:
    col = 1
    """
    1   1
    2   2
    3   3
    4   4
    5   5
    """
    while col <= row:
        # print("%d"%col)
        print("*",end="")
        col += 1
    # print("第%d行"%row)
    print("")# 换行
    row += 1