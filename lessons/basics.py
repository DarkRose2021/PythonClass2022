from re import MULTILINE


a = False
a = "string"
print(a)

a, b, c = 1, "Two", 3.0
print(a, b, c)

x, y, z = 1, 1, 1
x = y = z = 2
print(x, y, z)

print(x, y, z, end=' Done ')
print('next line')

# comment
'''
    comment
'''
"""
    comment
"""

multiline = '''
    string
    on
    many
    lines
'''
print(multiline)

# casting
m = int(1)
n = str(1)
o = float(1)
p = bool(1)
q = bool('True')
print(m, n, o, p, q)

print(type(m))

# strings
print('-' * 50)

name = "Katie"
fruit = "apple"
cost = 1.20

print(name, fruit, cost)
print(name + fruit + str(cost))
print(name + " purchased " + fruit + " for " + str(cost) + " dollars")
print(f'{name} purchased {fruit} for {cost} dollars')

together = 'a' 'b' 'c'
print(together)

print(len(together))

l = '   remove spaces   '
l1 = l.strip()
l2 = l.lstrip()
l3 = l.rstrip()
print(l1)
print(l2)
print(l3)

# indexes
s = 'abcdefg'
print(s[0])
print(s[3])
print(s[len(s)-1])
print(s[-1])
print(s[::-1])
print(s[0:6:2])
