#1. Write a Python program to
# - sum all the items in a list.
# - The list should be generated using list comprehension
# - The size of the list should be from a user input

list_length=int(input("Enter the length of the list: "))
work_list=[]

i=0
sum=0
while i < list_length:
    work_list.append(i)
    sum+=work_list[i]
    i+=1
print(f"The sum of {work_list} is {sum}")
