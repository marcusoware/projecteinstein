print("Hello, WELCOME TO OPENLAPS EDUCATIONAL INSTITUE \n")

print("1. Add Student")
print("2. View Students")
print("3. Update Students")
print("4. Delete Students")
print("5. Exit")

def choices():
    while True:
        
        option_c = input("Choose option: ") 
        if option_c == "1": 
            print("Enter Your Information") 
            get_studentinfo()
            
        elif  option_c == "2": 
            print("VIEW STUDENTS DETAILS UNDER DEVELOPMENT")
        elif  option_c == "3":
            print("UPDATE STUDENTS RECORDS UNDER DEVELOPMENT")
        elif  option_c == "4": 
            print("DELETE STUDENTS RECORDS UNDER DEVELOPMENT")
        elif  option_c == "5": 
            print("Thank you for using our school portal")
            break
        else:
            print("Invalid choice!")
            option_c = input("Enter a valid option: ") 


 #Function to collect input
students = []
def get_studentinfo():
    name = input("Enter Your  Name : \n")
    students.append(name)
    age = input("Enter Your age : \n")
    students.append(age)
    contact = input("Enter Your contact : \n")
    students.append(contact)
    email = input("Enter Your Email : \n")
    students.append(email)
    Fees = input("Enter Your Fees : \n")
    students.append(Fees)
    Loc = input("Enter Your Location : \n")
    students.append(Loc)
       # print(students)
    
    
    print("Student saved successfully!")

    with open("portal.txt","a") as file:
      for ss in students:
       file.write(ss)
    
    file.close()
choices()