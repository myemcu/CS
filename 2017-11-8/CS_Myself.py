# 面向对象Style：
#               规划过程、分类物件、操作对象、测试结果

# 规划过程
#                        涉及到的类                操作对象                        测试结果
# 1 警察安装子弹到弹夹    警察、弹夹、子弹   police.install_bullet(clip, bullet)     print(clip)
# 2 警察安装弹夹到枪     警察、枪、弹夹     police.install_clip(gun, clip)          print(gun)
# 3 警察持枪朝敌人开火   警察、敌人、枪     police.fire(gun, enemy)                 print(clip)、print(enemy)
# (3 子弹减少、敌人掉血)


class Role:
    def __init__(self, name):
        self.name = name

    def install_bullet(self, clip, bullet):
        clip.save_bullet(bullet)

    def install_clip(self, gun, clip):
        gun.save_clip(clip)

    # 警察开火、枪要射击、弹夹出子弹、子弹使敌人掉血
    def fire(self, gun, enemy):
        gun.shoot(enemy)


class Clip:
    def __init__(self, capacity):
        self.capacity = capacity
        self.bullet_list = []

    def save_bullet(self, bullet):
        # 子弹对象安装到弹夹列表(列表变化必须约束范围)
        if len(self.bullet_list) < self.capacity:
            self.bullet_list.append(bullet)

    def __str__(self):
        return "当前弹量：" + str(len(self.bullet_list)) + '/' + str(self.capacity)

    def out_bullet(self):
        if len(self.bullet_list) > 0:       # 列表变化必须约束范围
            bullet = self.bullet_list[-1]   # 从列表尾部读取一个子弹对象
            self.bullet_list.pop()          # 弹出 一个子弹对象
            return bullet
        else:
            return None


class Bullet:
    pass


class Gun:
    def __init__(self):
        self.clip = None

    def __str__(self):
        if not self.clip:
            return '枪无弹夹'
        else:
            return '枪有弹夹'

    def save_clip(self, clip):
        if not self.clip:
            self.clip = clip

    # 射击这个动作就是读取Clip类中的子弹对象
    def shoot(self, enemy):
        current_bullet = self.clip.out_bullet()
        if current_bullet:
            pass
        else:
            print('没子弹了，空枪!')


new_police = Role('警察')
new_clip = Clip(10)
new_bullet = Bullet()

print(new_clip)     # 显示当前弹量

# 警察装子弹到弹夹
for i in range(0, 5):
    new_police.install_bullet(new_clip, new_bullet)

print(new_clip)     # 显示当前弹量

new_gun = Gun()
# 警察安装弹夹到枪
print(new_gun)
new_police.install_clip(new_gun, new_clip)
print(new_gun)

# 创建敌人对象
new_enemy = Role('敌人')

# 警察朝敌人开枪————子弹减少
for j in range(0, 6):
    new_police.fire(new_gun, new_enemy)
    print(new_clip)
