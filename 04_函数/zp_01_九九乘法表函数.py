def multiple_table():

    # 函数multiple_table():
    # 需求 输出 九九乘法表
    # 1. 打印 9 行小星星
    row = 1

    while row <= 9:
        col =1
        while col <= row:
            print("%d * %d = %d "%(row,col,row*col),end="\t")# 制表转义字符，垂直方向对齐
            col +=1
        print("")
        row += 1
    # 2. 将每一个 * 替换成对应的行与列相乘