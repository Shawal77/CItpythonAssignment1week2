'''
Write a python program to input 5 subject marks and
calculate total marks, percentage and grade based on
following criteria
percentage less than 50 (Grade C)
percentage equal to 50 and less than 80 (Grade B)
percentage equal to 80 and more than 80 (Grade A)

'''
from re import T


subj=[0,0,0,0,0]
subj[0]=int(input("Enter marks for sub1:"))
subj[1]=int(input("Enter marks for sub2:"))
subj[2]=int(input("Enter marks for sub3:"))
subj[3]=int(input("Enter marks for sub4:"))
subj[4]=int(input("Enter marks for sub5:"))

total=0
grade=[]
for subjectMark in subj:
    total+=subjectMark
    if 0<=subjectMark and subjectMark<50:
        grade.append('C')
    elif 50<=subjectMark and subjectMark<80:
        grade.append('B')
    elif 80<=subjectMark and subjectMark<100:
        grade.append('A')

print(subjectMark)
print(total)
print(grade)
