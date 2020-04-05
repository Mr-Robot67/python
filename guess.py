import random

print("#####################")
print("\n")
print("Hi this is my  Python Script :) \nI'm Omar the Boy who wrote this script")
print("\n")
print("So How this Script Works you have to write numbers between 1 and 10")
print("then press enter ")
print("\n")
print("Have fun, Guessing :)")
print("\n")
print("#####################")
print("\n")

n = random.randint(1, 10)
print("I am thinking of a number between 1 to 10")

running = True
while running:
    guess_str = input("Take a guess ")
    guess = int(guess_str)
    if guess == n:
        print("Well Done That is Right")
        running = False
    elif guess < n:
        print("Try a bigger number ...")
    else:
        print("Don't try to be smart you piece of shit i said from 1 to 10 ")

input("Press any key to end this SHIT ...")
