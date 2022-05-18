import random
a=random.randint(1,10)

chances=0
while chances<5:
        guess=input("Enter your guess:")            
if (guess==a):
        print("You win!!")
elif (a>guess):
        print("Too low")
else:
        print("Too high")


        chances=chances+1
if (chances<5):
        print("You lose")
                