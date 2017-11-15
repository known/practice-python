'''
该模块是函数示例。
'''


def say(message, times=1):
    '''带默认值参数的函数'''
    print(message * times)


say('hello')
say('world ', 5)


def total(a=5, *numbers, **phonebook):
    '''
    a是单一变量
    *numbers是可变数量的元组参数
    **phonebook是可变数量的字典参数
    '''
    print('a ', a)

    # 遍历元组元素
    for item in numbers:
        print('item', item)

    # 遍历字典元素
    for key, value in phonebook.items():
        print(key, value)


print(total(10, 1, 2, 3, Jack=1123, John=2231, Tom=1560))
