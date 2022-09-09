'''
Write a program which will find all such numbers which
are divisible by 7 but are not a multiple of 5 between
2000 and 3200 (both included). The numbers obtained
should be printed in a comma-separated sequence on a
single line.
'''

i=2000
listt=[]
while i<=3200:
    if i%7 == 0 and i%5 != 0:
        listt.append(i)
    i+=1
for element in listt:
    print(element,end=',')
