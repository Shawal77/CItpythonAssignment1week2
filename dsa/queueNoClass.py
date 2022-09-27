myQueue=[]
def enqueue(lst: list,element)->list:
    lst.append(element)
    return element
def dequeue(lst: list):
    if len(lst)>0: return lst.pop(0)
    elif len(lst)==0:
        print('\nEmpty queue Cannot dequeue')
        return
def is_empty(lst: list)->bool:
    return len(lst)==0
def size(lst: list)->int:
    return len(lst)

print(is_empty(myQueue))
print(size(myQueue))
dequeue(myQueue)

enqueue(myQueue,1)
enqueue(myQueue,2)
enqueue(myQueue,3)
enqueue(myQueue,4)
enqueue(myQueue,5)
enqueue(myQueue,6)
enqueue(myQueue,7)
print(myQueue)

#removing first
print(f'\nRemoving element {dequeue(myQueue)} from myQueue')
print(myQueue)

print('\n',is_empty(myQueue))
print(size(myQueue))

print(f'\nRemoving element {dequeue(myQueue)} from myQueue')
print(myQueue)

print(f'\nRemoving element {dequeue(myQueue)} from myQueue')
print(myQueue)


[]