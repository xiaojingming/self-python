# 装饰器
from const import separator

def now():
    print('2025-09-02')

print(now.__name__) # now

print(separator)

def log(func):
    def wrapper(*args, **kw):
        print('function name:', func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now2():
    print('20250902')

now2()

print(separator)
