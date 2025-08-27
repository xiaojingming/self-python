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
