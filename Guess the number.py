from random import *

print("Guess the Number! You have 6 turns. \nYou'll be told if your guesses are to high or to low.")

def game():
    number = randint(1, 100)
    for turn in range(6):
        print("Turn", turn+1)
        guess= int(input("Guess a number between 1 and 100:"))
        if guess==number:
            print("You've guessed the number!")
            break
        elif guess<number:
            print("You've guessed to low!")
        elif guess>number:
            print("You've guessed to high!")
    nex()
def nex():
    again=input("Do you want to try again? y/n:")
    if again=="y":
        game()
    
game()


input()
