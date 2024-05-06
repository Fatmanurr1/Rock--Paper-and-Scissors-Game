#Rock, Paper and Scissors

import random

options = ['r', 'p', 's']
options2 = ['rock', 'paper', 'scissors']

print("As you enter the rock-paper-scissors game, you are greeted with the following instructions:")
print("Press 'r' for 'rock', 'p' for 'paper', and 's' for 'scissors' to begin. ")
print("Life = 3\nScore = 0")

score = 0
life = 3

print("------")

while life > 0:
    
    x = random.randint(0, 2)
    
    y = input()
    
    if options[x] == y:
        print("The computer said {}.".format(options2[x]))
        print("Draw")
        print("Life = {}\nScore = {}".format(life, score))
        
    elif options[x] == 'r':
        if y == 'p':
            score += 1
            print("The computer said {}.".format(options2[x]))
            print("You did it!")
            print("Life = {}\nScore = {}".format(life, score))
            
        elif y == 's':
            life -= 1
            print("The computer said {}.".format(options2[x]))
            print("Fail :(")
            print("Life = {}\nScore = {}".format(life, score))
            
        else:
            print("You can only press the keys r, p, and s.")
            
    elif options[x] == 'p':
        if y == 'r':
            life -= 1
            print("The computer said {}.".format(options2[x]))
            print("Fail :(")
            print("Life = {}\nScore = {}".format(life, score))
            
        elif y == 's':
            score += 1
            print("The computer said {}.".format(options2[x]))
            print("You did it!")
            print("Life = {}\nScore = {}".format(life, score))
            
        else:
            print("You can only press the keys r, p, and s.")
    
    else:
        if y == 'r':
            score += 1
            print("The computer said {}.".format(options2[x]))
            print("You did it!")
            print("Life = {}\nScore = {}".format(life, score))
            
        elif y == 'p':
            life -= 1
            print("The computer said {}.".format(options2[x]))
            print("Fail :(")
            print("Life = {}\nScore = {}".format(life, score))
            
        else:
            print("You can only press the keys r, p, and s.")

    print("------")

else:
    print("It was a good game!")
    