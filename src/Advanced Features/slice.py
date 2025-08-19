# 切片
seprator = '==============================>'

L = ['michael', 'sarah', 'tracy', 'bob', 'jack']

print(range(3))

for i in range(5):
    print(L[i])
    
print(seprator)

print(L[0:3])

print(L[:3])

print(L[1:3])

print(seprator)

L2 = range(100)

print(L2[:10])

print(L2[-10:])

print(L2[10:20])

print(L2[:10:2])

print(L2[:])

print(L2[::5])

print(seprator)

T1 = (0, 1, 2, 3, 4, 5)

print(T1[:])

print(seprator)

Str = "ABCDEFG"

print(Str[:3])

print(Str[::2])

Str2 = "   Hello, World!   "

print(Str2.strip())

print(Str2.lstrip())

print(seprator)

def trim(s):
    if (s == ''):
        return s
    
    start = 0
    end = len(s) - 1
    
    if (s[start] == ' '):
        return trim(s[start+1:])
    
    if (s[end] == ' '):
        return trim(s[start:end-1])
    
    return s

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
