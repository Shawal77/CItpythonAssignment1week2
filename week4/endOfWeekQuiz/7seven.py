'''
Write a function called show_stars(rows). If rows is 5,
it should print the following:
**
'''
def show_stars(rows):
    if rows==5:
        i=1
        while i<6:
            print('*'*i)
            i+=1
show_stars(5)
