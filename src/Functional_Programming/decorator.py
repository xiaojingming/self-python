# 装饰器
from const import separator
import time, functools

def now():
    print('2025-09-02')

print(now.__name__) # now

print(separator)

def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('function name:', text, func.__name__)
            print(args, kw)
            return func(*args, **kw)
        return wrapper
    return decorator

@log('test')
def now2(aa, bb, k=''):
    print('20250902')

now2(111, 222, k=11234)

print(now2.__name__) # wrapper

print(separator)

def log2(func):
    @functools.wraps(func)
    def wrapper():
        print(f'function name: {func.__name__}')
        func()
    return wrapper

@log2
def now3():
    print('20250903')

print(now3.__name__) # now3

print(separator)


def metric(fn):
    def wrapper(*args):
        start = time.time()
        value = fn(*args)
        end = time.time()
        print(f'exceute tiem: {end - start}')
        return value
    return wrapper

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')

