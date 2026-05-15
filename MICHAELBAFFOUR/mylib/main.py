# import maths
# def something():
#     return maths.addition(2,9)

# def everything():
#     pass
# print(something())

# a = ['orange', 'banana', 'apple', 'lemon']
# with open("app.txt","w") as file:
#     for fruit in a:
#           file.write(fruit+"\n")
#     file.close()

# with open("mik.txt", "w") as file:
#     print()
#     file.close()


#Create array
school = [] 
def student_name():
    name = input("Enter student's name: ")
    school.append(name)
    print(school)
student_name()

with open("school.txt", "w") as file:
    for name in school:
        file.write(name+"\n")
file.close()   


