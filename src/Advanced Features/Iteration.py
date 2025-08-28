# 迭代
separator = '===================>'

d = {
    'a': 1,
    'b': 2,
    'c': 3,
}

for key in d:
    print(key)
    
print(separator)

for value in d.values():
    print(value)
    
for [key, value] in d.items():
    print(key, value)
    
print(separator)

def findMinAndMax(L):
    if (len(L) == 0):
        return (None, None)
    
    min = L[0]
    max = L[0]
    
    for i in L:
        target = i
        
        if (min > target):
            min = target
        elif (max < target):
            max = target
    print(min, max)
    return (min, max)

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
