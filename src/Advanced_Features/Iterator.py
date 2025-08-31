# 迭代器
from collections.abc import Iterable

print(isinstance([], Iterable))

print(isinstance({}, Iterable))

print(isinstance('abc', Iterable))

print(isinstance((1, 2, 3), Iterable))

print(isinstance(100, Iterable)) # False

from collections.abc import Iterator

print(isinstance((x for x in range(10)), Iterator))

t1 = (x for x in range(10))
t2 = (1, 2, 3, 4, 5)

print(next(t1))
print(type(t2))
print(type(t1))
