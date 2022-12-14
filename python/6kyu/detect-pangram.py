#A pangram is a sentence that contains every single letter of the alphabet at least once. 
#For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses 
#the letters A-Z at least once (case is irrelevant).

#Given a string, detect whether or not it is a pangram. Return True if it is, False if not. 
#Ignore numbers and punctuation.

#My solution

import string

def is_pangram(s):
    
    alphabet = string.ascii_lowercase
    
    #We travel the entire alphabet, and check if each word is found in the "s" string.
    #If an element is not found, returns false.
    #If the entire loop is done and no False has been returned, we return True.
    for i in alphabet:
        if i not in s.lower():
            return False
    return True