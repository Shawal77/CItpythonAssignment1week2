#Python Bitwise Operators
#Bitwise operators are used to compare (binary) numbers:
a=9  #1001
b=11 #1011
#Operator	Name	Description
#   & 	AND	Sets each bit to 1 if both bits are 1
print("a&b = ",end="")
print(a&b)


#   |	OR	Sets each bit to 1 if one of two bits is 1
print("a|b = ",end="")
print(a|b)


#   ^	XOR	Sets each bit to 1 if only one of two bits is 1
print("a^b = ",end="")
print(a^b)


#   ~ 	NOT	Inverts all the bits
print("~a = ",end="")
print(~a)


#   <<	Zero fill left shift
#       Shift left by pushing zeros in from the right
#       and let the leftmost bits fall off
#print("<<a = ",end="-->")
#print(<<a)


#   >>	Signed right shift	Shift right by pushing copies
#       of the leftmost bit in from the left,
#       and let the rightmost bits fall off
#print(">>a = ")
#print(>>a)
