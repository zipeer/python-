class Animal:
    def eat(self):
        print("吃---")

    def drink(self):
        print("喝---")

    def run(self):
        print("跑---")

    def sleep(self):
        print("睡---")


class Dog(Animal):

    def bark(self):
        print("汪汪叫")

class XiaoTianQuan(Dog):

    def fly(self):
        print("我会飞")

    def bark(self):

        # 按照子类的需求，编写代码
        print("像神一样的叫唤")

        # 使用super（），调用父类中的方法
        # super().bark()

        # 2.x版本可以，但是在3.x版本不推荐
        # 父类名。方法（self）
        # Dog.bark(self)

        # 递归调用，死循环
        # XiaoTianQuan.bark(self)

        # 增加其他代码
        print("$%^$%^$%^$%^")


xtq = XiaoTianQuan()
# 子类重写，调用子类重写的方法
xtq.bark()