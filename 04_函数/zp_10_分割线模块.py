def print_line(char,times):
    """打印单行分割线

    :param char: 分割字符
    :param times: 分割次数
    """
    print(char * times)

def print_lines(char,times):
    """打印多行字符

    :param char: 分割字符
    :param times: 分割次数
    """
    row = 0

    while row < 5:
        print_line(char,times)# 函数的调用
        row += 1
name = "张朋"