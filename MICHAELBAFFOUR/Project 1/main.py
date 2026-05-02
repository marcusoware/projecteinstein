#taking userinput
from utils import register_std 
user_input = []
def main():
    while True:
     print("--- WELCOME TO GREATMIKE ACADEMY ---")
     print("1. REGISTER STUDENT")
     print("2. SEARCH FOR STUDENT")
     print("3. PAY FEES")
     print("4. EXIT")
    
     option = input ("Choose an option(1-4): ")
    #taking options
     if option == "1":
        print("--- WELCOME TO REGISTRATION PORTAL ---")
        register_std()
     elif option == "4":
        print("EXITING PROGRAM")
        break
     else:
        print("Invalid option. Please try again")
       

main()