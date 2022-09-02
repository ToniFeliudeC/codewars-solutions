#Welcome.

#In this kata you are required to, given a string, replace every letter with its position in the alphabet.

#If anything in the text isn't a letter, ignore it and don't return it.

#"a" = 1, "b" = 2, etc.

#Example
#alphabet_position("The sunset sets at twelve o' clock.")
#Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" ( as a string )

#My solution

import string

def alphabet_position(text):
    
    alphabet = string.ascii_lowercase
    newString = ""
    
    #We loop through the "text" string and check if it's in alphabet (aka check if it's not an space " ").
    #If it's in alphabet, we add the index of the letter on the alphabet + 1 (because indexes start from 0) + " "
    for i in text.lower():
        if i in alphabet:
            newString += str(alphabet.index(i) + 1) + " "
    
    #Finally we return the resulting string removing the last character, since it's always going to be a " ".
    return newString[:-1]

