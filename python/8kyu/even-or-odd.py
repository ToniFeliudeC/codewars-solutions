#Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.

#My solution

def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

#My 2nd solution

def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

#3rd solution I found and thought it was very clever.
#This solution works because even though we are not specifying if number % 2 equals 1 or 0, we can use the resulting value (1 or 0) from the condition as 
#a boolean.
#For example, if number % 2 results in 1, 1 is true boolean, if results in 0, is false boolean.

def even_or_odd(number):
    return "Odd" if number % 2 else "Even"

