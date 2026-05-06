#Task 1
# def patient_rec():
#  Name = 'John Smith'
#  print(Name)
#  Age = 20
#  print(Age)
#  Status = 'New Patient'
#  print(Status)
# patient_rec()

#Task 2
# name = input('Please tell us your name: ')
# colour = input('What is your favorite colour? ')
# print (name + ' likes '+ colour)

#Task 3
#age calculator
# name = input('Please enter your name: ')
# birth_month = input('Enter your birth month: ')
# current_year = input ('Enter the current year: ')
# birth_year = input ('Enter your birth year: ')
# # Calculating age
# Age = int(current_year) - int(birth_year)
# print(f'Hello {name},your age is {Age} and the record is {birth_month}/{birth_year}\n THANK YOU!')

#Task 4
#Taking user's weight
# user_weight = input('Enter your weight in pounds: ')
#Converting from lbs to kg
# weight_in_kg = int(user_weight) * float(0.454)
# print('your weight is '+ str(weight_in_kg) + 'kg')

#Task 5
# name = 'Michael'
# print(name[0:6])

# first = 'John'
# last = 'Smith'
# message = f'{first} {[last]} is a coder'
# print(message)

#Task 6
#conditionals
# age = 12
# child_age = int(input("Enter your child's age: "))
# if child_age <= age:
#     print('You get a child discount')
# else:
#     print('Regular Ticket price applies')

# print('END OF PROGRAM')

#Task 7
#Password checker
# password = input('Enter your Password: ')
# if len(password) >= 8:
#     print('Password is strong')
# elif len(password) <8:
#     print('Password is weak')

#Task 8
#checking temperature
# temperature = 30
# current_temp = int(input('Enter the current temperature: '))
# if current_temp < temperature:
#     print('Turning on heater')
#     print(f'Current Temperature: {current_temp}\u00b0F')

# else:
#     print('Temperature is comfortable')
#     print(f'Current Temperatuer: {current_temp}\u00b0F')

# print('Thermostat check complete')

#Task 9
#Working on student grade
# student_score = int(input('Enter your score: '))
# if student_score >= 90 and student_score <=100:
#     print('A')
# elif student_score >=80 and student_score <=89:
#     print('B')
# elif student_score >=70 and student_score <=79:
#     print('C')
# elif student_score >=60 and student_score <=69:
#     print('D')
# elif student_score <60 and student_score >=0:
#     print('F')
# else:
#     print('WRONG INPUT')

#Task 10
#Roller Coster and it's requirement 
# rider_height = int(input('Enter your height in inches: '))
# rider_age = int(input('Enter your age: '))
# if rider_height >= 48 and rider_age >=12:
#     print('You can ride')
# else:
#     print("Sorry you don't meet the height or age requirement")

#Task 11
# Current_temp = int(input('Enter your current temperature: '))
# is_raining = input('Is it raining (Y/N): ')
# if is_raining == 'No' and Current_temp >=65:
#     print('Great day for a picnic!')
# elif is_raining == 'Yes' or Current_temp < 32:
#     print('Stay indoors. Not a great day to be outside')
# else:
#     print('A decent enough day for a short walk')

#Task 12
#User's profile
# name = input('Enter your name: ')
# if len(name) <3:
#     print('name must be at least 3 characters')
# elif len(name) >50:
#     print('name can be a maximum of 50 characters')
# else:
#     print('name looks good!')

# #Task 13
# food = 457892578/3
# print(f'this price of the food is {food:,.3f}')

#Task 14
# numbers = [2, 4, 6, 8]
# for i in numbers:
#     square_of_number = i ** 2
#     print(square_of_number)

#Task 15
# friends = ['kwaku', 'Ben', 'Cleo']
# for name in friends:
#     print(f'Happy birthday {name}')

#Task 16
# for i in range(6,0, -1):
#     print(i)
# print('Blast off !')

# item_prices = [5.99, 3.49, 12.99, 2.99]
# total_cost = 0
# for item in item_prices:
#     total_cost += item
# print('Total cost:', total_cost)

for i in range(3,33,+3):
    print(i)

