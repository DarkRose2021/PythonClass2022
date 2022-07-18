from os import system
# string

abc = 'a b c d e f g'
letters = abc.split()
print(letters)

abc = 'a,b,c,d,e,f,g'
letters = abc.split(',')
print(letters)

j = ':'.join(letters)
print(j)

# replace
t = 'I saw the old man by the sea, old, old, old'
t1 = t.replace('old', 'young')
t2 = t.replace('old', 'young', 1)
print(t1)
print(t2)

# find
fruits = 'apple bandana orange bandana'
print(fruits.find('bandana'))
print(fruits.rfind('bandana'))
print(fruits.find('bandana', 10))
f1 = fruits.split()
for fruit in f1:
    if fruit == 'bandana':
        print(fruit)

system('cls')

# lists
myList = ['apple', 'banana', 'cherry', 'peach', 'banana', 1, True, 192.88]
print(myList[1])
myList[1] = 'pear'
print(myList[:1])
print(myList[1:3])
print(myList[::-1])

myList.append('New')
print(myList)

myList.pop()
print(myList)
myList.pop(1)
print(myList)
myList.remove('peach')
print(myList)
del myList[0]
print(myList)
# myListList = [
#     ['a', 'b', 'c']
#     [1,2,3]
# ]

# initialized lists
l = []
l.append(True)
l2 = list()

system('cls')

# searching list
myList = ['apple', 'banana', 'cherry', 'peach', 'banana', 1, True, 192.88]
print(myList.index('banana'))
print(myList.index('banana'), 2)
print(myList.count('banana'))
print('peach2' not in myList)

# copy a list from memory
myList = ['apple', 'banana', 'cherry', 'peach']
myListCopy = myList
print(myList)
print(myListCopy)
myList.append('pear')
print(myList)
print(myListCopy)
print('-' * 50)

# copy a list
myList = ['apple', 'banana', 'cherry', 'peach']
myListCopy = myList.copy()
print(myList)
print(myListCopy)
myList.append('pear')
print(myList)
print(myListCopy)

system('cls')

# tuples
t1 = tuple()
t1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(t1[0])

t2 = 1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7
print(t2)

t3 = ('string', 1, True)
print(t3)

notATuple = ('no')
print(notATuple)

isATuple = ('yes',)
print(isATuple)

#unpacking tuple
t4 = ('name', 10, True)
v1, v2, v3 = t4
print(v1, v2, v3)

a = 5
b = 4
c = 3

system('cls')

if a > b and b > c:
    print('yes')

if a > b or c > nonvariable:
    print('yes')

if a > b:
    pass