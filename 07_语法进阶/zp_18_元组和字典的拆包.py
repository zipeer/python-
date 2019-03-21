def demo(*args,**kwargs):

    print(args)
    print(kwargs)

# 元组变量/字典变量直接传递到函数内部时使用拆包

gl_nums = (1,2,3)
gl_dict = {"name":"小明","age":18}

# demo(gl_nums,gl_dict)
# 拆包语法
demo(*gl_nums,**gl_dict)

demo(1,2,3,name="小明",age=18)