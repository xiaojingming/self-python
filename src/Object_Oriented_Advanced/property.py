# @property 内置装饰器

class Student:
    def get_score(self):
        return self.score
    
    def set_score(self, score):
        if not isinstance(score, int):
            raise ValueError('score must be integer!')
        
        if score < 0 or score > 100:
            raise ValueError('score must betwee 0 ~ 100!')
        
        self.score = score
        
s = Student()

s.set_score(99)

print(s.get_score())  # 99

# 直接通过s.score来获取

class Student2:
    @property
    def score(self):
        return self.__score
    
    @score.setter
    def score(self, score):
        if not isinstance(score, int):
            raise ValueError('score must be integer!')
        
        if score < 0 or score > 100:
            raise ValueError('score must betwee 0 ~ 100!')
        
        self.__score = score

s2 = Student2()

s2.score = 100

print(s2.score) # 100

class Screen(object):
    @property
    def resolution(self):
        return self.__width * self.__height
    
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        self.__width = value
        
    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, value):
        self.__height = value

# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')

