#project1
#School_portal_system
#takes_user_details_into_school_portal_system
all_students=[]# A list to hold everyone
def Register_Student():
    name =input("Enter your name:")
    age =int(input("Enter your age:"))
    contact=(input("Enter your contact:"))
    email =input("Enter your email:")


def save_student(name, age, contact, email):
    student_data={"name": name, "age": age, "contact": contact, "email": email}
    all_students.append(student_data)
    print("Student save to database")


def Search_Student():
    Search_Name=input("Enter student name to search")
    for Student in all_students:
     if Student["Name"].lower()== Search_Name.lower():
        print("\n---Student Found---")
        print(f"Name:{Student['Name']}")
         




