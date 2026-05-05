#global hashes
separator = "=" * 45

def main():

    while True:
        #welcome message
        print(f"\n{separator}")
        print("Welcome to future leaders accademy.".title())
        print("Please select an option below to proceed:".title())
        print(f"{separator}\n")

        #available options to choose from
        options = ["register", "about the school", "courses Offered", "payment plans", "exit"]

        for index, option in enumerate(options, start=1):
            print(f"{index}. {option.title()}")

        #taking user's choice for the above options
        user_choice = input("Please choose one of the above options(1-5) to proceed: ").strip()

        #logics for each of the above options
        if user_choice == '1':
            pass
        elif user_choice == '2':
            pass
        elif user_choice == '3':
            pass
        elif user_choice == '4':
            pass
        elif user_choice == '5':
            print("\nThank you for visition Future Leaders Accademy. Goodbye!👋")
            break
        else:
            print("Invalid input. Pleas try again by entering  a number from 1-5")
main()