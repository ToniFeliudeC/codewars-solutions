##Find the missing letter

#Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

#You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
#The array will always contain letters in only one case.

#Example:

#['a','b','c','d','f'] -> 'e' ['O','Q','R','S'] -> 'P'

#["a","b","c","d","f"] -> "e"
#["O","Q","R","S"] -> "P"
#(Use the English alphabet with 26 letters!)

#Have fun coding it and please don't forget to vote and rank this kata! :-)

#I have also created other katas. Take a look if you enjoyed this kata!

#My solution

import string

def find_missing_letter(chars):
        
        #On this variables we will store an strings with the entire alphaber lower and uppercase.
        alphabet = string.ascii_lowercase
        upperAlphabet = string.ascii_uppercase
        
        
        #We check if the letters of "chars" are upper or lowercase, to determine if we have to consult from "alphabet" or "upperAlphabet"
        #Once we know that, we trabel the entire "chars" array, and check if the ahead letter is in "chars" or not.
        if chars[0].islower():
            for i in chars:
                if alphabet[alphabet.index(i)+1] not in chars:
                    return alphabet[alphabet.index(i)+1]
        else:
            for i in chars:
                if upperAlphabet[upperAlphabet.index(i)+1] not in chars:
                    return upperAlphabet[upperAlphabet.index(i)+1]