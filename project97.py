import random

print(" Number Guessing Game")
number=random.randint(1,9)
chances=0
print("guess a number between 1 and 9- ")
while chances<5:
    guess=int(input("enter your guess between 1 and 9"))
    if guess==number:
        print("Congratulation You Won")
        break
    elif guess<number:
        print("your guess was too low")

    else :
        print("your guess was too high")
    chanes=chances+1

if not chances<5:
    print("you lose!!! the number is",number)


    