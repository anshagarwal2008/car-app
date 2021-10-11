import random
print("you have to think what number is the running speed of car")
number=random.randint(1,9)
chances=0

while chances<5:
    guess=int(input("guess a number between 1-9 "))
    if guess==number:
        print("good,car at normal speed")
    chances+=1
if not chances < 5:
    print("You Lose !! car is very fast",number)