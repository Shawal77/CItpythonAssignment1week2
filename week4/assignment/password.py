'''Password Generator Python Project
Create a program that generates a random password for the user
. Ask the user how long they want their password to be, and how
many letters and numbers they want in their password. Have a mix
of upper and lowercase letters, as well as numbers and symbols.
The password should be a minimum of 6 characters long.'''
import string
import random


def main():
    length=int(input("Enter length of the password"))
    if length < 6:
        print("Password must be greater than 6")
        main()
    letters=int(input("how many letters"))
    #nums=int(input("how many nums"))
    alphabet_list = list(string.ascii_letters)
    print(alphabet_list)
    nums_list=[1,2,3,4,5,6,7,8,9,0]
    i=0
    j=0
    passwordArray=[]
    while i<letters:
        index=random.randint(0,len(alphabet_list)-1)
        passwordArray.append(alphabet_list[index])
        i+=1
    while j<(length-letters):
        index=random.randint(0,9)
        passwordArray.append(str(nums_list[index]))
        j+=1
    random.shuffle(passwordArray)
    passw=''.join(passwordArray)
    print(passw)
main()
