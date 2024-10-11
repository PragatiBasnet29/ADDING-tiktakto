#swapping two numbers without using temp variable

num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num1=num1+num2
num2=num1-num2
num1=num1-num2
print("After swapping first Number is: ", num1)
print("After swapping second Number is: ", num2)