'''
Write a python program to sort array element in the
ascending/descending order
'''
def ascending_sort(shuffled_array):
    i=0
    while i < len(shuffled_array):
        j=i+1
        while j < len(shuffled_array):
            if shuffled_array[i]>shuffled_array[j]:
                var=shuffled_array[i]
                shuffled_array[i]=shuffled_array[j]
                shuffled_array[j]=var
            j+=1
        i+=1
    return shuffled_array

def descending_sort(shuffled_array):
    i=0
    while i < len(shuffled_array):
        j=i+1
        while j < len(shuffled_array):
            if shuffled_array[i]<shuffled_array[j]:
                var=shuffled_array[i]
                shuffled_array[i]=shuffled_array[j]
                shuffled_array[j]=var
            j+=1
        i+=1
    return shuffled_array

def main():
    arraayt=[7,2,5,8,9,7,4,1,25]
    print(ascending_sort(arraayt))
    print(descending_sort(arraayt))

if __name__=='__main__':
    main()
