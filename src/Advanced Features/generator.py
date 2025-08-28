# 生成器

from const import separator

R = range(1, 11)

g1 = (g * g for g in R)

for g in g1:
    print(g)

print(separator)

def fib(max):
    n, a, b = 0, 0, 1
    
    while(n < max):
        print(b)
        
        a, b = b, a + b
        n = n + 1
        
    return 'done'

print(fib(6))

print(separator)

def fib2(max):
    n, a, b = 0, 0, 1
    
    while(n < max):
        yield(b)
        
        a, b = b, a + b
        n = n + 1
        
    return 'done'

print(fib2(6))

print(separator)

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 3
    print('step 3')
    yield 5

o = odd()

print(next(o))
print(next(o))
print(next(o))

print(separator)

for g in odd():
    print(g)
    
print(separator)

g2 = fib2(6)

while True:
    try:
        x = next(g2)
        print('g2:', x)
    except StopIteration as e:
        print('Generator return value:', e, e.value)
        print(e)
        break

print(separator)

def triangles():
    n = 0
    while n < 10:
        n += 1
        l = [1 if x == 0 or x == n - 1 else l[x - 1] + l[x] for x in range(0, n)]
        yield l
        

# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)

if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')
