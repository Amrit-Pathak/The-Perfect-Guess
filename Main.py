import random

computer_guess= random.randint(1,100)
n= -1
guesses=1
while (n!= computer_guess):
    
    n=int(input("Enter your guess: "))
    if (n<computer_guess):
        print("Guess a higher number")
        guesses+=1
    elif (n> computer_guess):
        print("Guess a lower number")
        guesses+=1

print(f"You have guessed the right number {computer_guess} on your {guesses}th guess.")