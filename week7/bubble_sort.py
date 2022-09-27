import timeit
def bubble_sort(array: list):
    print(f'Initial length: {len(array)}')
    for i in range(len(array)):
        for j in range(len(array)-1-i):
            if array[j]>array[j+1]:array[j],array[j+1]=array[j+1],array[j]
    return array

def optimised_bubble_sort(array: list):
    print(f'Initial length: {len(array)}')
    for i in range(len(array)):
        swapped=False
        for j in range(len(array)-1-i):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
                swapped=True
            if not swapped:break
    return array
d=[9,8,7,6,5,4,3,1,2]
print(timeit.timeit('bubble_sort(d)'))
