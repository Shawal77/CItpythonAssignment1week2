'''
Write a python program to fetch only Email ID from text
file which include following fields -:
Name
Mobile Number
Roll Number

Email ID
'''
import re

text = "Mablire Shawal 0780221186 12345 mbalireshawal@gmail.com"

emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text)
print(emails)
