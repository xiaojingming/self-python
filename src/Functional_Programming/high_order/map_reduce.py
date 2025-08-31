# map
from functools import reduce
from Functional_Programming.const import separator

r1 = range(1, 10)

l1 = list(r1)

print(type(l1))

print(separator)

l2 = list(map(str, r1))

print(l2)

print(separator)

def normalize(name):
    return name.capitalize()

# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

print(separator)

def prod(L):
    def sum(cur, next):
        return cur * next
    return reduce(sum, L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

print(separator)

def str2float(s):
    [intVal, floatVal] = s.split('.')
    return reduce(lambda x, y: x * 10 + y, map(lambda x: int(x), intVal)) + 10 ** (-len(floatVal)) * reduce(lambda x, y: x * 10 + y, map(lambda x: int(x), floatVal))

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')


