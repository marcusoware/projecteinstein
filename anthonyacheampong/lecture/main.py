def display_invoice(username, amount, due_date):
    print("Hello", (username))
    print("Your bills of", (amount), "was issued on the", (due_date))
    
#display_invoice("Tony", "$400", "13/02/2026")


def catcry():
    i = 0
    while i < 5:
     print("meow")
     i += 1

#catcry()

def take_name():
    name = input("Enter your name : ")
    while len(name) < 7:
        print("name is less than 7 ")
        name = input("what is your name : ")
    
    print(name)
        
#take_name()


def check_odd_numbers():
    num = int(input("Enter number : "))
    while num % 2 == 0:
        print("number not odd")
        num = int(input("Enter number : "))
    print(num)
    
#check_odd_numbers()

 
lfruits = ["orange", "mango", "cow", "pawpaw", "pineapple", "grapes"]
lfruits [0] = "banana"
#print(lfruits)


vegetables = lfruits
#print(vegetables)
#print(vegetables[3])

cars = ['toyota', 'benz', 'honda', 'hundai', 'python', 'avtr']
for i in (cars):
    print(i)