# Katie King 2022
# A Year to Remember
from os import system
import random
system('cls')

counter = 0
nextIndex = 0

# Questions
QandA = [
    ("the start of the Revolutionary War", 1775), 
    ("the United States Constitution signed", 1783), 
    ("President Lincoln assassinated", 1865), 
    ("Theodore Roosevelt's first day in office as President of the United States", 1901), 
    ("the beginning of World War II", 1939), 
    ("the first personal computer introduced", 1975), 
    ("the Berlin Wall taken down", 1989), 
    ("gold discovered in california", 1848), 
    ("texas annexed", 1845), 
    ("the cotton gin invented", 1794)
]

# Shuffle questions
random.shuffle(QandA)

for q in QandA:
    invaildInput = True
    while invaildInput:
        try:
            print("In what year was " + q[0]+ "?")
            answer = int(input())
        except:
            print("Please only enter numbers")
            invaildInput = True
        else:
            invaildInput = False 

    if answer == q[1]:
        counter += 10
        print("Correct! The year was " + str(q[1])+ ". +10 points!")
        print("Your score is now "+str(counter))
    elif answer in (range(q[1], 6+q[1])) or answer in (range(q[1]-5, q[1])):
        counter += 5
        print("Close! The correct year was " +str(q[1])+ ". +5 points!")
        print("Your score is now "+str(counter))
    elif answer in (range(q[1], 11+q[1])) or answer in (range(q[1]-10, q[1])):
        counter += 2
        print("A bit too far. The correct year was " +str(q[1])+ ". +2 points!")
        print("Your score is now "+str(counter))
    elif answer in (range(q[1], 21+q[1])) or answer in (range(q[1]-20, q[1])):
        counter += 1
        print("You're more than 10 years off. The correct year was " +str(q[1])+ ". +1 point!")
        print("Your score is now "+str(counter))
    elif answer >= (21+q[1]) or answer <= (q[1]-21):
        print("Way too far off! The correct year was " +str(q[1])+ ". No points.")
        print("Your score is now "+str(counter))
    else:
        print("error")

if counter >= 70:
    print("You did great! Your score is " +str(counter))
elif counter in range(60,70):
    print("At least you didn't go below 59 points. You scored " +str(counter))
else:
    print("Your score is" +str(counter)+ ". You didn't do very well. Thanks for trying!")