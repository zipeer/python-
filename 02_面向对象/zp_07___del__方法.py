class Cat:
    def __init__(self,new_name):

        self.name = new_name
        print("%s来了"% self.name)

    def __del__(self):
        # 在对象最后一次使用后执行
        print("%s我去了"% self.name)

tom = Cat("Tom")

print(tom.name)
# 删除对象
# 最后一次使用tom对象
del tom
print("-"*50)
