#Katie King 2022
import random
from os import system

questions = [
    ('What is your favortie color: ', 'Blue',['Red', 'Blue', 'Yellow', 'Green']),
    ('What is your favortie car: ', 'Chevy', ['Honda', 'Toyota', 'Ford', 'Chevy']),
    ('What is your favortie food: ', 'Apples', ['Apples', 'Blueberries', 'Bananas', 'Pickles'])
]

random.shuffle(questions)

try:
    for q in questions:
        system('cls')
        random.shuffle(q[2])
        print(q[0])
        i = 1
        for a in q[2]:
            print(f'{i}. {a}')
            i+=1
        answer = int(input('>>> '))

        if q[2][answer-1] == q[1]:
          print("Good Job")
        else:
            print('You Lose')
            break
        print()
        input('Hit Enter for next question')
except:
    print('Invalid Input')