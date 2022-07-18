# loops
# for and while
from os import system

system('cls')

i = 1
while True:
    print(i)
    i += 1
    if i > 9:
        break

print('-'*50)

i = 1
while i < 10:
    print(i)
    i += 1
system('cls')

# while True:
#     answer = input('>>> ').lower()
#     if answer == 'quit':
#         break

i = 0
while i < 10:
    i += 1
    if i >= 3 and i <= 5:
        continue
    print(i)

print('-'*50)

i = 1
while i < 6:
    print(i)
    i += 1
    if i > 3:
        break
else:
    print('out of the loop')


system('cls')

# for loop
fruits = ['apple', 'banana', 'cherry']
s = 'this is a really long string for something'
for c in s:
    print(c)

print('-'*50)

for b in 'bananas':
    print(b)
    
print('-'*50)

for t in (1,2,3,4,5):
    print(t)

system('cls')

for i in range(10):
    print(i)

print('-'*50)

for i in range(2,8):
    print(i)
print()

for i in range(2,8,2):
    print(i)

system('cls')

for i in range(8,2, -1):
    print(i)
print()

for i in reversed(range(2,8)):
    print(i)

print()

adj = ['red', 'big', 'tasty']
fruits = ['apple', 'banana', 'cherry']

for a in adj:
    for f in fruits:
        print(a,f)
        print('-'*14)