num1=float(input("Enter first number "))
operatorD=input("Choose one operator(+,-,*,/) ")
num2=float(input("Enter second number "))

if operatorD == "+":
    answer=num1+num2
elif operatorD == "-":
    answer=num1-num2
elif operatorD == "*":
    answer=num1*num2
elif operatorD == "/":
    answer=num1/num2
else:
    print("Enter a valid operator")
print(num1,operatorD,num2,"=",answer)
