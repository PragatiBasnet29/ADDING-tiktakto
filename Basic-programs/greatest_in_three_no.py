
a=int(input("Enter first number:")) # TAKING INPUT FOM USER
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))

if a>b or a>c:
    print("First no is greater than second and third no")

    if b>a or b>c:
        print("Second no is greater than first and third no")

else:
    print("Third no is greater than first and second no")       