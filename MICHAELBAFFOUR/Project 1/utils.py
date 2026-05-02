def register_std():
    name = input("Enter Student's name: ")
    age = int(input("Enter Student's age: "))
    fees = float(input("Enter Student's fees: "))
    city = input("Enter your city: ")
    print("Student registered successfully")
    return {"name": name, "age": age, "fees": fees, "city": city}
    