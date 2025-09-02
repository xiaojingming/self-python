# 返回函数

from functools import reduce
from const import separator

def calc_sum(*args):
    return reduce(lambda x,y : x+y, args)

print(calc_sum(1, 2, 3, 4, 5, 6))

print(separator)

def inc():
    x = 0
    def fn():
        nonlocal x
        # 仅读取x的值:
        x = x + 1
        return x
    return fn

f = inc()
print(f()) # 1
print(f()) # 2

print(separator)

def createCounter():
    x = 0
    def counter():
        nonlocal x
        x = x + 1
        return x
    return counter

# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
