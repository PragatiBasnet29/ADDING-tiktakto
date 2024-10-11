#   To check if a year is a leap year or not

year = int(input("Enter a year: ")) # TAKING INPUT FOM USER
if year%4 ==0:
    if(year%100==0):
        if(year%400==0):
            print("This is a leap year")
        else:
            print("This is Not a leap year")
    else:
        print("This is a leap year")
else:
    print("This is Not a leap year")