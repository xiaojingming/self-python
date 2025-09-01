# sorted
from Functional_Programming.const import separator

l1 = [36, 5, -12, 9, -21]

print(l1, type(l1))

print(separator)

print(sorted(l1)) # [-21, -12, 5, 9, 36]
print(sorted(l1, key=abs)) # [5, 9, -12, -21, 36]

print(separator)

l2 = ['bob', 'about', 'Zoo', 'Credit']

print(sorted(l2)) # ['Credit', 'Zoo', 'about', 'bob']
print(sorted(l2, key=str.lower)) # ['about', 'bob', 'Credit', 'Zoo']
print(sorted(l2, key=str.lower, reverse=True)) # ['Zoo', 'Credit', 'bob', 'about']

print(separator)

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    name, age = t
    return name

L2 = sorted(L, key=by_name)
print(L2) # [('Adam', 92), ('Bart', 66), ('Bob', 75), ('Lisa', 88)]

L2 = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_score(t):
    name, age = t
    return age

L3 = sorted(L2, key=by_score)
print(L3) # [('Bart', 66), ('Bob', 75), ('Lisa', 88), ('Adam', 92)]

