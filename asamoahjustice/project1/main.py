import json

#global hashes
separator = "=" * 45
divider = "-" * 45

#welcome message
print(f"\n{separator}")
print("Welcome to future leaders academy.".title())
print("Please select an option below to proceed: ".title())
print(f"{separator}\n")

def main():

    while True:
        print("\nAvailable options to choose from".title())

        #available options to choose from
        options = ["register for a course", "about the school", "courses Offered", "payment plans", "search for a student", "exit"]

        for index, option in enumerate(options, start=1):
            print(f"{index}. {option.title()}")

        #taking user's choice for the above options
        user_choice = input("\nPlease an option(1-5) from above to procede: ").strip()

        #logics for each of the above options
        if user_choice == '1':
            confirm_userinfo()

        elif user_choice == '2':
            show_schoolinfo()
            input("\nPress any key to continue: ")
        elif user_choice == '3':
            show_courses()
            input("\nPress any key to continue: ")
        elif user_choice == '4':
            pass
        elif user_choice == '5':
            search_forstudent()
            input("\nPress any key to continue: ")
        elif user_choice == '6':
            print("\nThank you for visiting Future Leaders Academy. Goodbye!👋")
            input("\nPress any key to continue: ")
            break
        else:
            print("\nInvalid input. Please try again by entering  a number from 1-5")


#function for confirming user's info
def confirm_userinfo():
    
    #calling the function taking the user's info
    result = get_user_info()

    #exiting to the main function if the user entered '0' in the above function
    if result == None:
        return
    
    #unpacking the information in the above function
    name, age, contact, location = result

    try:
        #initialinzing user info in a list
        student_info = []

        #reading old saved student info into all students so they are not over written
        with open("school_system.json", "r") as file:
            all_students = json.load(file)


    except FileNotFoundError:
        all_students = []

    #creating a variable for the info ones and use the append to make it simple
    new_student = {
    "name":     name,
    "age":      age,
    "contact":  contact,
    "location": location
    }

    #adding the new student info into the variable student info for displaying purposes
    student_info.append(new_student)

    #displaying the student info so he/she can verify if correct
    print("\n")
    for student in student_info:
        print(f"{'-' * 4}Here are your details. Please Review{'-' * 5}")
        print(f"{divider}")
        print(f"Name:     {student['name']}")
        print(f"Age:      {student['age']}")
        print(f"Contact:  {student['contact']}")
        print(f"Location: {student['location']}")
        print(divider)

    #either edit, cancel or confirm the above details
    confirmation_list = ["confirm", "edit", "cancel"]
    print("\n")
    for index, procede in enumerate(confirmation_list, start=1):
        print(f"{index}. {procede.capitalize()}")
    print("\n")

    confirmation = input("Please choose an option(1-3) to procede: ")

    #append and save their info if they choose to confirm
    if confirmation == '1':
        #
        print("Congratulations 🎉🎊! Your registration was successful.")

        all_students.append(new_student)

        #writing everything back to the file
        with open("school_system.json", "w") as file:
            json.dump(all_students, file, indent=4)

    #let them re-enter thier details if they choose to edit
    elif confirmation == '2':
        result = get_user_info()
        name, age, contact, location = result 

    #else cancel
    else:
        return




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


#function for displaying courses offered
def show_courses():
    courses = [
        ["software development",     2, 7500],
        ["graphic design",           1, 3750],
        ["cyber security",           1, 3750],
        ["nertwork engineering",     2, 7000],
        ["business administration",  1, 3000],
        ["fashion design",           1, 3000]
    ]

    width1 = 5 #width of the space after first header column
    width2 = len("Duration(Years)") + width1 #width spaces after the duration column header
    width3 = 30 #30 width spaces after each course duration

    print(f"\n{divider}{'-' * 22}")
    print(f"{'#':<{width1}} {'Course':<{width3}} {'Duration(Years)':<{width2}} {'Fees(GHS)'}")
    print()
    
    for i, (course, duration, fees) in enumerate(courses, start=1):
        print(f"{i:<{width1}} {course.title():<{width3}} {duration:<{width2}} {fees:,.2f}")

def show_paymentplans():
    pass


#function for taking user's info
def get_user_info():
    while True:
        try:
            #givin the user a choice to go back to the main menu
            user_input = input("\nPlease enter your name, age, contact and location. " \
            "Separate each input with a space before" \
            " the next input(eg. Jonh 26 02560000 Adum) or enter 0 to go to main menu: ")

            if user_input == '0':
                return None #exit to the main function if the input is 0
            
            name, age, contact, location = user_input.split()
            age = int(age)
            location = location.upper()
            name = name.upper()
            
            return name, age, contact, location #if anything goes through, return out of the loop

        except Exception as e:
            print(f"{e}: Please enter a valid input(NB: age must be a number)")


#function for searching for a student
def search_forstudent():
    search = input("Please enter full name of student(eg, Kofi): ").upper()

    #reading all the students info to search from
    with open("school_system.json", "r") as file:
        all_students = json.load(file)

    #assuming no student has been found
    found = False

    #looping through all students
    for student in all_students:
        #using in not == specifically so that you can type the 1st three letters and can get
        #a match if you don't remember the whole name
        if search in student['name']:
            found = True
            print()
            print("Student Found! Here are the details:")
            print(f"Name:       {student['name']}")
            print(f"Location:   {student['location']}")

    #this runs only if no student is found 'cause if a student is found, the found 
    #inside  the if statement will be true and when it gets here, not makes it false so it does't run
    if not found:
        print("No student found with that name. Please try again")
main()