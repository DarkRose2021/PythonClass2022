# dictionaries
from os import system

dict1 = {'key': 'value'}

dict2 = {
    'brand': 'Ford',
    'model': 'mustang',
    'year': 1964,
    'favorate': False,
    'colors': ['red', 'blue']
}

print(dict2)
print(dict2['brand'])
dict2['model'] = 'thunderbird'

print(dict2)
print(len(dict2))

print('-'*50)

dict3 = dict()
dict3['name'] = 'Scott'
dict3['age'] = 25
print(dict3)
print(dict2)

print('-'*50)

cars = [
    {'brand': 'toyota', 'make': 'mustang', 'year': 1964},
    {'brand': 'ford', 'make': 'f-150', 'year': 2015},
    {'brand': 'honda', 'make': 'prelude', 'year': 1989}
]
print(cars)

system('cls')

# sets
set1 = {'apple', 'bananas', 'orange', 'bananas'}

print(set1)

list1 = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3,
         3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5]
list2 = set([1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3,
            3, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5])
set2 = set(list1)
list1 = set2


u = set('hello dont refer to me')
print(u)

#union and intersection
a = {1,2,3}
b = {4,5,6}
print(a.union(b))
print(a.intersection(b))
