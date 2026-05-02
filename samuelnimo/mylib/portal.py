#function creating
students = []
def school():
    #funtion for userinput
    st_input = input("Please Enter your Name : ")
    students.append(st_input)
    print(students)
    
school()    

with open("mmpp.txt","w") as file:
    for st_input in students:
      file.write(st_input)
    
file.close()
    

    