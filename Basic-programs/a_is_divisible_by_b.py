# To check weather one number is divisible by other or not 

a=int(input("Enter First number:")) # TAKING INPUT FOM USER
b=int(input("Enter second number:")) # TAKING INPUT FOM USER

if a%b==0:
    print("First no is divisible by second no ")

elif b%a==0:
    print("Second no is divisible by first no ")

else:
    print("Both numbers are not divisible by each other")