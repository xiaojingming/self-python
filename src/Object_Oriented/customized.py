# 定制类
from const import separator

class Student:
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return f'Student Object name: {self.name}'
        
        
print(Student('xjm')) # <__main__.Student object at 0x7c05997ff320>
print(Student('xjm')) # Student Object name: xjm

print(separator)

class Fib:
    def __init__(self):
        self.a, self.b = 0, 1
        
    def __iter__(self):
        return self
    
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100:
            raise StopIteration()
        return self.a
    
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = 0 if n.start == None else n.start
            end = n.stop
            
            a, b = 1, 1
            l = []
            for x in range(end):
                if x >= start:
                    l.append(a)
                a, b = b, a + b
            return l
            
    def  __getattr__(self, attr):
        if attr == 'age':
            return lambda: 25
    
    
for n in Fib():
    print(n)

print(separator)

f = Fib()

print(f[5]) # 8

print(f[0:5])
print(f[:10])
print(f.age()) # 25