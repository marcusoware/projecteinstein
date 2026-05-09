#Guessing game
import random

print("Welcome to the Number Guessing Game\n"
      "Guess a number from 1-100\n"
      "If you guess wrong you will be given a hint to guess higher or lower,\n"
      "Keep going till you get it RIGHT!")

computer=random.randint(1,100)
user_guess=int(input('Now enter a number from 1 to 100:\n'))
attempts=0

while user_guess!=computer:
    attempts+=1
    
    if user_guess>computer:
        print('Guess lower') 
    else:
        print('Guess higher')

    user_guess=int(input('Enter a number from 1 to 100:\n'))
        
attempts+=1        
print(f'You guessed the right number in {attempts} attempts!')            