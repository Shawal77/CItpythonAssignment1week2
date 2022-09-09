
'''
Write a python program to find the maximum and minimum
 value in a given 2-D array
'''
from audioop import maxpp


two_dArray=[[7,8],[8,19]]

max=two_dArray[0][0]
for element in two_dArray:
    for number in element:
        if number>max:
            max=number
print(max)

