# A list to store student data
# students = []

# def main():
#     while True:
#         print("--- WELCOME TO THE SCHOOL PORTAL ---")
#         print("1. Register")
#         print("2. Search for a student")
#         print("3. Delete information")
        
#         choice = input("Choose an option (1-3): ")

#         if choice == '1':
#             name = input("Enter Student Name: ")
#             age = input("Enter Student Age: ")
#             fees= float(input("Enter Student Grade: "))
#             city = input("Enter your city: ")

#         with open('records.txt', 'w') as file:
#             file.write(f'Name: {name}'
#                        f'Age: {age}'
#                        f'Fees: {fees}'
#                        f'City: {city}'
#             )
#         with open('records.txt', 'r') as file:
#             print(file.read())

#         elif choice == '2':
#             if not students:
#                 print("Not registered yet.")
#             else:
#                 print("\n--- Registered Students ---")
#                 for s in students:
#                     print(f"Name: {s['Name']} | Age: {s['Age']} | fees: {s['fees']} | city: {s['city']} ")

#         elif choice == '3':
#             print("Closing portal...")
#             break
#         else:
#             print("Invalid input, please try again.")

# if __name__ == "__main__":
#     main()
import time
start = time. time()
n = 1
while n < 1000:
    print(n)
    n += 1
end = time.time()
print ("'elapse time =' end - start")


