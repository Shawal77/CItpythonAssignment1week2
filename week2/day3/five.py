# 5. Write a Python program to generate and
# print a list except for the first 5 elements,
# where the values are square of numbers between 1 and 30 (both included)

gen_list = [x**2 for x in range(1,31)]#range(start,stop,step)
print(gen_list[5:31])#except first five elements
