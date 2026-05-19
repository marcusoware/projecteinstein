from constant import divider, separator

#school info
def show_schoolinfo(): 
    print(f"\n{separator}")
    print(f"{'#':<5} about future leaders academy".title())
    print("Future Leaders Academy is a top-tier institution dedicated" \
          " to providing quality education to students across Ghana.")
    print()
    print("Location  : Kumasi, Ashanti Region")
    print("Phone     : +233 24 000 0000")
    print("Email     : info@futureleaders.edu.gh")
    print("Hours     : Mon - Fri, 8:00am to 5:00pm")
    print()


#function for displaying courses offered
def show_courses():
    courses = [
        ["software development",     2, 7500],
        ["graphic design",           1, 3750],
        ["cyber security",           1, 3750],
        ["nertwork engineering",     2, 7000],
        ["business administration",  1, 3000],
        ["fashion design",           1, 3000]
    ]

    width1 = 5 #width of the space after first header column
    width2 = len("Duration(Years)") + width1 #width spaces after the duration column header
    width3 = 30 #30 width spaces after each course duration

    print(f"\n{divider}{'-' * 22}")
    print(f"{'#':<{width1}} {'Course':<{width3}} {'Duration(Years)':<{width2}} {'Fees(GHS)'}")
    print()
    
    for i, (course, duration, fees) in enumerate(courses, start=1):
        print(f"{i:<{width1}} {course.title():<{width3}} {duration:<{width2}} {fees:,.2f}")

def show_paymentplans():
    pass
