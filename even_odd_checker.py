#Exercise 2: Even or Odd Number Checker

#Write a Python program that asks the user to enter a number and checks whether it is even or odd.
    #Example:
#Enter a number: 7
#The number is odd.
#Enter a number: 10
#The number is even.

#Solution:

#Ask the user to enter a number.

code = True

while code:
    def even_odd_checker(number):
        
        if number % 2 == 0:
            return "The number is even"
        else:
            return "The number is odd"

    number = int(input("Enter a number: "))
    results = even_odd_checker(number)
    print(results)
    user_input = input("Enter [Q] to quit or any key to continue: ")

    if user_input.upper() == "Q":
        print("Goodbye!")
        code = False
