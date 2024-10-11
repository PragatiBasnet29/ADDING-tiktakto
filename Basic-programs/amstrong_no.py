# To check whether a no is amstrong no or not   

num = int(input("Enter a number: "))  # Taking input from user


# Storing the value of num in temp variable
temp = num

# Initializing sum to 0
sum = 0     

#taking the length of the number
order = len(str(num))

while temp>0:               #Logic of amstrong no is that the sum of the cube of the digits of a number is equal to the number itself
    digit = temp%10
    sum += digit**order
    temp //= 10

if num == sum:
    print(num, "is an Armstrong number")

else:
    print("It is not an Armstrong number")

