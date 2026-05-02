#for i in range(rows, 0,-1):
    #print(" " * (rows - i - 1) + "*" * (2 * i - 1))
    
    #print(" " * (rows - i - 1) + "*" * i)
    #print(" " * (rows - i ) + "*" * (2 * i - 1))
# students = ['SAMUEL NIMO', 'ALICE KUMAH','MOSES ABAGRI', 'SELINA GYAMFI']
# #print(students[0]) 
# #print(students[1])  
# #print(students[2])  
# #print(students[3])

# #for student in students:
#     #print(student)   
# #for student in range(len(students)):
#     #print(student + 1,students[student])  
# from random import choice 
# coins = choice(["Heads","Tails"])

# print(coins)
# import time
# start = time.time()
# n = 1
# while n <=1000:
#     n+=1
# print(n)
# end = time.time()
# el = end - start
# print(el)
# #
# nums = [2,7,9,11,15]

# target = 9

# for i in nums:
#     for j in nums[i]:
#         if i + j == target:
#             print(i,j)

nums = [2, 7, 9, 11, 15]
target = 22

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print(nums[i], nums[j])
