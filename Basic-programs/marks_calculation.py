#to calculate the percentage of marks obtained by thwe student 

a=int(input("Enter the marks of the Maths subject: "))
b=int(input("Enter the marks of the Hindi subject: "))
c=int(input("Enter the marks of the English subject: "))
d=int(input("Enter the marks of the Science subject: "))
e=int(input("Enter the marks of the Sanskrit subject: "))

sum= a+b+c+d+e
percentage= (sum/500)*100
 
print("The total marks obtained by the student is: ", sum)
print("The percentage of marks obtained by the student is: ", percentage)

if percentage>90:
    print("The student has secured A grade")

elif percentage>80:
    print("The student has secured B grade")

elif percentage>70:
    print("The student has secured C grade")    

elif percentage>60:
    print("The student has secured D grade")

else:
    print("The student need to work hard to secure good grades")
