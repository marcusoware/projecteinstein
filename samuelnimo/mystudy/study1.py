# def areaofcircle():
#     length = int(input("Enter the length "))
#     height = int(input("Enter the height "))
#     pi = 3.421
#     area = pi * length * height
#     print(area)

# areaofcircle()
#guessing game 
#mainfunction creating
import random
def guess_gamemain():
    
    guessnumber = random.randrange(1, 100)
    take_number = input("Please Enter with 1 - 100 : " )
    guessattempt = 5
    print(guessnumber)
    
    #user number function
def usernumber(take_number,guessnumber):
    #Please Enter with 1 - 100 
    while take_number not in guessnumber:
        take_number = input("Please Enter with 1 - 100 : " ) 
    return take_number
def main_guesscondition(take_number,guessnumber):
    if take_number != guessnumber:
        guessattempt=+1
        if guessattempt == 5:
            return "YOU DONT HAVE ANY ATTEMPT AGAIN !! TRY AGAIN LATER"
        exit
#computer choice function
def computer_guess(guessnumber): 
    c_guess = random.choice(guessnumber)
    return c_guess
    
guess_gamemain()
    