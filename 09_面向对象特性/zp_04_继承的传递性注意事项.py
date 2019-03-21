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

class Cat(Animal):
    def catch(self):
        print("我会抓老鼠")

# 创建一个哮天犬对象
xtq = XiaoTianQuan()

xtq.fly()
xtq.brak()
xtq.eat()

# xtq.catch()
# 不能调用没有直接关联的类中的方法