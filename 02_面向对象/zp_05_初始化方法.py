class Cat:
    def __init__(self):

        print("这是初始化方法")

        # 添加属性
        # self.属性名 = 属性的初始值
        # 这种方法有智能提示，之前在外部添加的没有
        self.name = "Tom"

    def eat(self):
        print("%s爱吃鱼"% self.name)


# 使用类名（）创建对象的时候，会自动调用初始化方法 __init__
# 创建对象
tom = Cat()

print(tom.name)