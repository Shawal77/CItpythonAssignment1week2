# 4. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
# Sample List : `['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']`

sample_list=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
sample_list.remove(sample_list[0])
sample_list.remove(sample_list[4-1])
sample_list.remove(sample_list[5-1-1])
print(sample_list)
