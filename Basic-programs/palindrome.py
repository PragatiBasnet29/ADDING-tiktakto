#To check whether a no is palindrome or not

num = int(input("Enter a Number: "))   # Taking input from user

reverse_num = int(str(num)[::-1])  # Reversing the number


if num == reverse_num:
    print(num, "is a Palindrome number")    # If the number is equal to its reverse then it is a palindrome number

else:
    print("It is not a Palindrome number")  # If the number is not equal to its reverse then it is not a palindrome number    