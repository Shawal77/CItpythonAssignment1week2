# 3. Write a Python program to remove duplicates from a list,
#  given list `fruits = ["Apple", "Banana", "Melon", "Banana", "Cherry", "Banana"]`

#answer1
print("Answer1")
fruits = ["Apple", "Banana", "Melon", "Banana", "Cherry", "Banana"]
print(fruits)
i=0
while i<len(fruits):
    p=0
    while p<len(fruits):
        if i==p:#avoid checking the current as its always true
            p+=1
            continue
        if fruits[p]==fruits[i]:
            fruits.remove(fruits[i])
            continue
        p+=1
    i+=1
print(fruits)


#answer2
print("Answer2")
fruits = ["Apple", "Banana", "Melon", "Banana", "Cherry", "Banana"]
print(fruits)
answer=set(fruits)
fruits=list(answer)
print(fruits)



