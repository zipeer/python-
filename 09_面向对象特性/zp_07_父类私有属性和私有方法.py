class A:
    def __init__(self):

        self.num1 = 100
        self.__num2 = 200

    def __test(self):
        print("私有方法%d%d"%(self.num1,self.__num2))

class B(A):

    def demo(self):

        # 在子类的对象方法中不能访问父类的私有属性和方法
        # print("访问父类的私有属性%d"%self.__num2)

        # 调用父类的私有方法
        # self.__test()
        pass

# 创建子类对象
b = B()
print(b)

b.demo()

# 在外界访问私有属性和方法
# print(b.__num2)
# b.__test()