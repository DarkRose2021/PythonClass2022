# Katie King 2022
from os import system
import json
from textwrap import indent

system('cls')

menu = ('''
    add [First Name] [Last Name] [Phone]    (add a new contact record)
    list                                    (List all records)
    find [value]                            (find and show the first record that matches the search)
    del [value]                             (delete the first record that matches the search)
    quit                                    (Quit the CLI)
''')

people = []

def find_person(name):
    for person in people:
        if person['First Name'].lower() == name.lower() or person['Last Name'].lower() == name.lower():
            return person
            break
        
    print('Person not found')

def dump():
    with open('db.json', 'w') as file1:
        json.dump(people, file1, indent=1)

def add(fname, lname, phone):
    global people
    people.append({'First Name': fname, 'Last Name': lname, 'Phone Number': phone})
    
def list():
    for person in people:
        print(person['First Name'], person['Last Name'], person['Phone Number'])
        print('-'*60)
    
def find(name):
    if find_person(name):
        person = find_person(name)
        print(person['First Name'], person['Last Name'], person['Phone Number'])
        print('-'*60)

def delete(name):
    if find_person(name):
        person = find_person(name)
        fname = person['First Name']
        lname = person['Last Name']
        people.remove(person)
        print(fname, lname+ ' was removed')
    
print(menu)

try:
    with open('db.json', 'r') as file1:
        people = json.load(file1)
except:
    pass

while True:
    commandLine = input('>>> ')
    values = commandLine.split()
    command = values[0]
    args = values[1:]
    try:
        if command == 'add':
            add(args[0], args[1], args[2])
            dump()
            print(args[0], args[1]+ ' was added')            
        elif command == 'list':
            list()
        elif command == 'find':
            find(args[0])
        elif command == 'del':
            delete(args[0])
            dump()                
        elif command == 'quit':
            print('Closing Command Line')
            exit()
        else:
            print(menu)
    except IndexError:
        print(menu)