class Cat():

    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫爱喝水")

tom = Cat()

tom.eat()
tom.drink()

print(dir(Cat))
print(tom)

addr = id(tom)
print("%x" % addr)
print(tom)

lazy_cat = Cat()

lazy_cat.eat()
lazy_cat.drink()
print(lazy_cat)