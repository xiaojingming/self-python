# 访问限制

class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def get__name(self):
        return self.__name
        
bart = Student('xjm', 27)

print(bart.get__name()) # xjm

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender
        
    def get_gender(self):
        return self.__gender
    
    def set_gender(self, gender):
        self.__gender = gender

# 测试:
bart2 = Student('Bart', 'male')
if bart2.get_gender() != 'male':
    print('测试失败!')
else:
    bart2.set_gender('female')
    if bart2.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')

