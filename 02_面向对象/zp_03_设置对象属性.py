class Cat():

    def eat(self):
        # 哪一个对象调用的方法：self就是哪一个对象的引用
        print("%s爱吃鱼" %self.name)

    def drink(self):
        print("%s爱喝水"% self.name)

# 创建对象
tom = Cat()

# 直接添加属性，不推荐
tom.name = "Tom"

tom.eat()
tom.drink()

print(tom.name)
print(dir(Cat))
print(tom)

addr = id(tom)
print("%x" % addr)
print(tom)

# 再创建一个对象
lazy_cat = Cat()

lazy_cat.name = "大懒猫"

lazy_cat.eat()
lazy_cat.drink()
print(lazy_cat)