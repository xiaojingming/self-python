# 列表生成式
import os

from const import separator

r1 = range(1, 11)

l1 = list(r1)

print(l1)

print(separator)

l2 = []

for i in r1:
    l2.append(i * i)
    
print(l2)

print(separator)

l3 = [i * i for i in r1]

print(l3)

print(separator)

l4 = [i * i for i in r1 if (i % 2 == 0)]

print(l4)

print(separator)

l5 = [s1 + s2 for s1 in 'ABC' for s2 in 'XYZ']

print(l5)

print(separator)

l6 = [d for d in os.listdir('.')]

print(l6)

d1 = { 'a': 'A', 'b': 'B', 'c': 'C' }

for (key, value) in d1.items():
    print(key, value)

print(separator)

l7 = [f'{key}={value}' for key, value in d1.items()]

print(l7)

print(separator)

l8 = ['Hello', 'World', 'IBM', 'Apple']

l9 = [s.lower() for s in l8]

print(l9)