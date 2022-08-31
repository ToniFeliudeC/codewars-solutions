#Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

#Example
#create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
#The returned format must be correct in order to complete this challenge.

#Don't forget the space after the closing parentheses!

#My solution

def create_phone_number(n):
    
    #We make a "template" of the string we want to return, marking the spots where numbers are going to be placed, with an "x".
    phoneString = "(xxx) xxx-xxxx"

    #Now we travel the "numbers" array, and use each element to replace the very NEXT "x" we find in our phoneNumber string.
    for i in n:
        phoneString = phoneString.replace("x",str(i),1)
    
    
    return phoneString