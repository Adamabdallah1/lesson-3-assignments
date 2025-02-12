#1) Exercise 1: Movie Ticket Price CalculatorWrite a Python program that asks the user for their age and determines the price of a movie ticket based on the following rules:
#- If the user is , the ticket is
#- If the user is , the ticket costs .
#- If the user is , the ticket costs .
#- If the user is , the ticket costs .
#Example:
#Enter your age: 8
#The ticket price is $5.

#Solution:
#Ask the user to enter their age.
code = True

while code:
    def movie_ticker_price(age):
        #Determine the price of the movie
        if age <= 10:
            print(f"The ticket price of age {age} is $5.")
        elif age <= 16:
            print("The ticket price of age {age} is $7.")
        elif age <= 18:
            print("The ticket price of age {age} is $9.")
        else:
            print("The ticket price of age {age} is $12.")

    age = int(input("Enter your age: "))

    results = movie_ticker_price(age)
    print(results)
    
    user_input = input("Enter [Q] to quit or any key to continue: ")
    if user_input.upper() == "Q":
        print("Goodbye!")
        code = False