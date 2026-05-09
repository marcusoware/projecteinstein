#taking userinput
user_input = []
def main():
    user_name = input('Enter your name: ')
    print(user_input)
    user_age = input('Enter your age: ')
    print(user_input)
    user_email = input('Enter your email: ')
    print(user_input)
    user_fees = float(input('Enter your fees: '))
    print(user_input)
    user_location = input('Enter your city/address: ')
    print(user_input)

with open("main.txt", "a") as file:
        file.write(user_input+"\n")
file.close()

main()