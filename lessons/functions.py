# function

def myFunct(value1=-1, value2=-1):
    if value1 != -1 and value2 != -1:
        return f'value is {value1}, {value2}'
    else:
        return 'no value'

print(myFunct())