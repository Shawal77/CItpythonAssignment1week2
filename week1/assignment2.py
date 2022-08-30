#converts temp
#choidce of user
#use if to check Cto F or F to C

print("Which conversion do you want?")
print("1.) Chose 1 for celsius to fahrenheit")
print("2.) Chose 2 for fahrenheit to celsius")
print("Enter integers 1 or 2")

answer=int(input())
print("Enter a value")
value=int(input())

if answer == 1:
    result = (value*9/5)+32
    print("it is "+str(result)+"fahrenheit")
elif answer == 2:
    result = (value-32)*5/9
    print("it is "+str(result)+"celsius")
else:
    print("invalid")

