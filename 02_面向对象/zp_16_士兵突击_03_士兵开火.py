class Gun:
    def __init__(self,model):

        # 枪的型号
        self.model = model

        # 子弹的数量
        self.bull_count = 0

    def add_bullet(self,count):

        self.bull_count += count

    def shoot(self):

        # 判断子弹数量
        if self.bull_count <= 0:
            print("[%s]没有子弹了。。。"% self.model)

            return


        # 发射子弹
        self.bull_count -= 1

        # 提示发射信息
        print("[%s] 突突突。。。 [%d]" % (self.model,self.bull_count))

class Soldier:
    def __init__(self,name):

        # 姓名
        self.name = name
        # 枪
        self.gun = None

    def fire(self):

        # 判断是否有枪
        # is 判断两个变量引用的对象是否为同一个
        # == 判断引用变量的值是否相等
        if self.gun is None:
            print("[%s]还没有枪。。。"% self.name)

            return

        # 高喊口号
        print("冲啊。。。[%s]"% self.name)

        #让枪装子弹
        self.gun.add_bullet(50)

        # 让枪发射子弹
        self.gun.shoot()

# 创建枪对象
ak47 = Gun("AK47")



# 创建许三多
xusanduo = Soldier("许三多")
xusanduo.gun = ak47
xusanduo.fire()
print(xusanduo.gun)