import random

n=random.randrange(1, 20)

new=[]
print("Hello! What is your name?")
name=str(input())
print("Well, ", name, "I am thinking of a number between 1 and 20.\nTake a guess.")
a=int(input())
new.append(a)
def guess(n, a, new):
    if n==a:
        print ("Good job, ", name, "! You guessed my number in ", len(new) , "guesses!")
        return
    if a>n:
        print ("Your guess is too much\nTake a guess.")
        a=int(input())
        new.append(a)
        return guess(n, a, new)
    if a<n:
        print ("Your guess is too low\nTake a guess.")
        a=int(input())
        new.append(a)
        return guess(n, a, new)
guess(n, a, new)