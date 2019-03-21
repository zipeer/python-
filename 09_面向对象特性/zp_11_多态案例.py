class Dog(object):

    def __init__(self,name):
        self.name = name

    def game(self):
        print("%s蹦蹦跳跳玩耍"%self.name)

class XiaoTianQuan(Dog):

    def game(self):
        print("%s飞到天上去玩耍"%self.name)

class Person(object):

    def __init__(self,name):
        self.name = name

    def game_with_dog(self,dog):

        print("%s和%S快乐的玩耍" % (self.name,dog.name))

        dog.game()

# 创建一个狗对象
wangcai = Dog("旺财")
# 创建小明对象
xiaoming = Person("小明")

# 让小明和狗玩耍
xiaoming.game_with_dog(wangcai)
