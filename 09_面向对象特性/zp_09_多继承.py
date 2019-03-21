# 注意事项：如果父类之间存在同名的方法，尽量不要使用多继承
class A:

    def demo(self):
        print("A--demo方法")

    def test(self):
        print("A--test方法")

class B:
    def demo(self):
        print("B--demo方法")

    def test(self):
        print("B--test方法")


class C(B,A):
    """多继承可以让子类拥有多个父类的方法"""

    pass

c = C()

c.test()
c.demo()

print(C.__mro__)