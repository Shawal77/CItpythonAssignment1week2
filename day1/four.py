# print numbers that,
#   divisible by 5
#   skip greater than 150
#   stop loop for greater than 500
#[12,75,150,180,145,525,50]
nums=[12,75,150,180,145,525,50]
for num in nums:
    if num>500 and num%5==0:
        break
    if num>150 and num%5==0:
        continue
    if num%5==0:
        print(num)

