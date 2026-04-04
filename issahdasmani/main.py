# first task
name = input("what is your name?")



# task two
name = "Issah"
print("hello, name")

# task 3
#takes user_name in upper
name = input("what is your name").upper()
print(f"hello{name}")


#task 4
#user_name concatenation 
def user_name():
    first_name =input("what is your first_name")
    last_name =input("what is your last_name")
    return(f"your full_name is{first_name } {last_name}")
print(user_name())

#task 5
#days_of _the _week_user_input
def days_of_the_week():
    day =input("Enter day of the week")
    if day =="Monday":
        return("Monday")
    elif day =="Tuesday":
        return("Tuesday")
    elif day =="Wednesday":
        return("wednesday")
    elif day =="Thursday":
        return("Thursday")
    elif day =="Friday":
        return("Friday")
    elif day =="Saturday":
        return("Saturday")
    elif day =="sunday":
        return("Sunday")
    else:
        return("Invalid")
# ()



# task_6
# build_calculator
def calculator(a,b,c = "add"):
    if c == "add":
        return a+b
    elif c == "sub":
        return a-b
    elif c == "div":
        return a/b
    elif c == "mul":
        return a*b
    else: 
        return "Invalid input"
print(calculator(5,6,"add"))



def  whileloop():
    n=0
    while n<5:
        print("meow")
        n+=1
whileloop()
    


        