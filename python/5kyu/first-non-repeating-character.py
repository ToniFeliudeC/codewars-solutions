#Write a function named first_non_repeating_letter that takes a string input, and returns the first character that is not repeated anywhere in the string.

#For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the string, and occurs first in the string.

#As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.

#If a string contains all repeating characters, it should return an empty string ("") or None -- see sample tests.

#My solution

def first_non_repeating_letter(string):
    
    #We make a new variable with the string as lowercase, so that we can make the function case insensitive.
    lowerString = string.lower()
    
    #Travel the given string, from beginning to end, and return the element whose number of times appearing in string is 1.
    #If the entire string is travelled and no return has been done, we return "", as no element fits the condition.
    for i in range(len(string)):
        if lowerString.count(string[i].lower()) == 1:
            return string[i]
    
    return ""