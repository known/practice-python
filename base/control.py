'''
该模块是控制流实例。

控制流语句如下：
if
while
for
break
continue
'''


def guessnumber():
    '''猜数字游戏'''
    number = 23
    running = True

    while running:
        guess = int(input('猜整数：'))

        if guess == number:
            print('恭喜您，猜中啦！')
            running = False
        elif guess < number:
            print('No，小啦')
        else:
            print('No, 大啦')
    else:
        print('猜数字结束！')


guessnumber()
print('游戏结束')
