'''
面向对象继承。
'''

class ShcoolMember:
    '''学校成员。'''

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def tell(self):
        '''告诉我你的信息。'''
        print('我是{}，{} 岁。'.format(self.name, self.age), end=' ')


class Teacher(ShcoolMember):
    '''老师。'''

    def __init__(self, name, age, salary):
        ShcoolMember.__init__(self, name, age)
        self.salary = salary

    def tell(self):
        ShcoolMember.tell(self)
        print('薪水有 {:d}'.format(self.salary))


class Student(ShcoolMember):
    '''学生。'''

    def __init__(self, name, age, marks):
        ShcoolMember.__init__(self, name, age)
        self.marks = marks

    def tell(self):
        ShcoolMember.tell(self)
        print('成绩是 {:d}'.format(self.marks))


t = Teacher('张三', 40, 30000)
s = Student('李四', 25, 75)
members = [t, s]
for member in members:
    member.tell()
