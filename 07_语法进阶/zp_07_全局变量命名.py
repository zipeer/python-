# 全局变量前加gl_前缀
gl_num = 10
gl_title = "张朋"
gl_name = "小明"
def demo():

    # 如果局部变量和全局变量名字相同，局部变量下面会出现灰色虚线
    num = 99

    print("%d" % num)
    print("%s" % gl_title)
    print("%s" % gl_name)


demo()

# 不能定义在函数后面，应定义在所有函数的上方，这时所有的函数都可以
# 使用全局变量了
