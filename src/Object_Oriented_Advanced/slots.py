# 使用__slots__
from types import MethodType

class Student():
    # 限制实例属性，但集成时无效
    __slots__ = ('name', 'age', 'set_age')

s = Student()

s.name = 'xjm'

print(s.name) # xjm

def set_age(self, age):
    self.age = age
    
s.set_age = MethodType(set_age, s)

s.set_age(27)

print(s.age) # 27

# s.score = 100

# print(s.score)

class GraduateStudent(Student):
    __slots__ = ('score')

g = GraduateStudent()

g.score = 99
g.name = 'sss'

print(g.score, g.name) # 99 sss
