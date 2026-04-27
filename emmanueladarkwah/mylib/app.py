# a=open('app.txt','r')

# with open('app.txt','r') as file:
#     print(file.readlines()) 

# with open('app.txt','r') as file:
#     for line in file.readlines():
#         print(line)

# fruits= ['mango', 'orange','banana','pear','grape']
# with open('app.txt','w') as file:
#     for item in fruits:
#         file.write(item+'\n')
# file.close()

# with open('rammatu.txt','w') as file:
#     print():
# file.close()

#Array to store user input
school=[]

#Function to accept the user input
def std_name():
    name=input('Enter students name:\n')
    school.append(name)

std_name()

#storing data into txt file
with open('app.txt','a') as file:
    for item in school:
        file.write(item+'\n')
file.close()