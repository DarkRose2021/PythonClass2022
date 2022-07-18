# BYO CLI
from os import system
system('cls')

menu = '''
Enter one of the following commands
    echo [value]                -returns the input
    add [number]  number        -returns the sum of 2 numbers

    quit                        -quits the CLI
'''

def echo(value1):
    print(value1)
    return True

def add(num1, num2):
    result = 0
    try:
        result = int(num1) + int(num2)
    except:
        pass
    return result


print(menu)

while True:
    commandline = input(">>> ")

    values = commandline.split()
    command = values[0]
    args = values[1:]

    if command == 'echo':
        if(echo(args)):
            print("echo function success")
    elif command == 'quit':
        print("thanks for visiting")
        exit()
    elif command == 'add':
        print(add(args[0], args[1]))
    else:
        print(menu)
