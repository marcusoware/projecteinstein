import json
#global hashes
separator = "=" * 45
divider = "-" * 45

def main():

    while True:
        #welcome message
        print(f"\n{separator}")
        print("Welcome to future leaders academy.".title())
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
            take_userinfo()
            input("")
        elif user_choice == '2':
            show_schoolinfo()
            input("")
        elif user_choice == '3':
            pass
        elif user_choice == '4':
            pass
        elif user_choice == '5':
            print("\nThank you for visiting Future Leaders Academy. Goodbye!👋")
            break
        else:
            print("\nInvalid input. Please try again by entering  a number from 1-5")

#function for taking user's info
def take_userinfo():
    try:
        name, age, contact, location = input("\nPlease enter your name, age, contact and location. Separate each input with a space berfore" \
    " the next input(eg. Jonh 26 02560000 Adum): ").split()
        age = int(age)
        location = location.upper()
        name = name.upper()

    except Exception as e:
        print(f"{e}: Please enter a valid input(NB: age must be a number)")

    #initialinzing user info in a list
    student_info = []

    #storing each student info in a dictionary
    student_info.append({
        "name":     name,
        "age":      age,
        "contact":  contact,
        "location": location
    }
    )

    #saving student info as json instead of txt
    with open("school_system", "w") as file:
        json.dump(student_info, file, indent=4)

    #reading student info saved as json
    with open("school_system.json", "r") as file:
        school_system = json.load(file)
    
    #displaying the student info so he/she can verify if correct
    for student in student_info:
        print(f"\n{divider}")
        print(f"Name:     {student['name']}")
        print(f"Age:      {student['age']}")
        print(f"Contact:  {student['contact']}")
        print(f"Location: {student['location']}")
        print()


#school info
def show_schoolinfo(): 
    print(f"\n{separator}")
    print(f"{'#':<5} about future leaders academy".title())
    print("Future Leaders Academy is a top-tier institution dedicated" \
          " to providing quality education to students across Ghana.")
    print()
    print("Location  : Kumasi, Ashanti Region")
    print("Phone     : +233 24 000 0000")
    print("Email     : info@futureleaders.edu.gh")
    print("Hours     : Mon - Fri, 8:00am to 5:00pm")
    print()

main()