'''
机器人模块。
'''


class Robot:
    '''机器人。'''

    # 机器人数量
    population = 0

    def __init__(self, name):
        '''初始化数据'''
        self.name = name
        print('初始化 {}'.format(self.name))
        Robot.population += 1

    def die(self):
        '''我挂了'''
        print('{} 挂了'.format(self.name))
        Robot.population -= 1

        if Robot.population == 0:
            print('{} 是最后一个挂的。'.format(self.name))
        else:
            print('还有 {:d} 个机器人在工作。'.format(Robot.population))

    def say_hi(self):
        '''来自机器人的问候'''
        print('您好，我叫 {}'.format(self.name))

    @classmethod
    def how_many(cls):
        '''打印出当前机器人口'''
        print('我们有 {:d} 个机器人！'.format(cls.population))


r1 = Robot('R2-D2')
r1.say_hi()
Robot.how_many()

r2 = Robot('C-3PO')
r2.say_hi()
Robot.how_many()

r1.die()
r2.die()
Robot.how_many()
