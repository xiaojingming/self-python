# 类和实例

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def print_name(self):
        print(self.name)
        
    def print_age(self):
        print(self.age)

bart = Student('xjm', 27)

bart.print_name()
bart.print_age()
