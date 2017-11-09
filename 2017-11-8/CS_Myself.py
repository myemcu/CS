# 面向对象Style：
#               规划过程、分类物件、操作对象、测试结果

# 规划过程
#                          涉及到的类                操作对象                        测试结果
# 警察安装子弹到弹夹      警察、弹夹、子弹    police.install_bullet(clip, bullet)     print(clip)
# 警察安装弹夹到枪        警察、枪、弹夹     police.install_clip(gun, clip)          print(gun)
# 警察持枪朝敌人开火      警察、敌人、枪     police.fire(gun, enemy)                 print(clip)、print(enemy)


class Role:
    def __init__(self, name):
        self.name = name

    def install_bullet(self, clip, bullet):
        clip.save_bullet(bullet)


class Clip:
    def __init__(self, capacity):
        self.capacity = capacity
        self.bullet_list = []

    def save_bullet(self, bullet):
        # 子弹对象安装到弹夹列表
        if len(self.bullet_list) < self.capacity:
            self.bullet_list.append(bullet)

    def __str__(self):
        return "当前弹量：" + str(len(self.bullet_list)) + '/' + str(self.capacity)


class Bullet:
    pass


new_police = Role('警察')
new_clip = Clip(10)
new_bullet = Bullet()

print(new_clip)     # 显示当前弹量

# 警察装子弹到弹夹
for i in range(0, 5):
    new_police.install_bullet(new_clip, new_bullet)

print(new_clip)     # 显示当前弹量
