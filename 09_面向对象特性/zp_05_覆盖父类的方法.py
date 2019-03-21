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

    def brak(self):
        print("汪汪叫")

class XiaoTianQuan(Dog):

    def fly(self):
        print("我会飞")

    def brak(self):
        print("叫的跟神一样")

xtq = XiaoTianQuan()
# 子类重写，调用子类重写的方法
xtq.brak()