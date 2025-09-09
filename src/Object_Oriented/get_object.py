# 获取对象信息
import types

print(type(123)) # <class 'int'>
print(type('str')) # <class 'str'>
print(type(None)) # <class 'NoneType'>
print(type(abs)) # <class 'builtin_function_or_method'>
print(int == type(123)) # True

print(isinstance([1, 2, 3], (tuple, list)))

def dict2bean(obj, dic):
    for k, v in dic.items():
        if hasattr(obj, k):
            obj.k = v  #这里无法修改类中a,d的值，使用setattr(obj,k,v)就可以

class obj():
    d=1
    def __init__(self,a):
        self.a=a


dic={'a':3,'d':88}
x=obj(12)
dict2bean(x, dic)

print(x.a)
print(x.d)