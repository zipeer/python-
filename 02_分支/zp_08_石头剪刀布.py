# 注意导包时要在最顶部和Java一样
import random # 随机工具包

# 从控制台输入要出的拳 —— 石头（1）／剪刀（2）／布（3）
player = int(input("请输入你要出的拳—— 石头（1）／剪刀（2）／布（3）："))

# 电脑 随机 出拳 —— 先假定电脑只会出石头，完成整体代码功能
computer = random.randint(1,3)
print("玩家选择的拳是%d - 电脑出的拳是%d"%(player,computer))

# 比较胜负
# 游戏规则
if ((player == 1 and computer ==2)
        or (player == 2 and computer ==3)
        or (player == 3 and computer == 1)):
    print("恭喜你赢了！")
elif player == computer:
    print("平局！")
else:
    print("很遗憾，你输了！")