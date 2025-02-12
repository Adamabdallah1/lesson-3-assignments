#Exercise 2: Even or Odd Number Checker

#Write a Python program that asks the user to enter a number and checks whether it is even or odd.
#Example:
#Enter a number: 7
#The number is odd.
#Enter a number: 10
#The number is even.

#Solution:

#Ask the user to enter a number.
user = int(input("Enter a number: "))

#Check if the number is even or odd.
if user % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")