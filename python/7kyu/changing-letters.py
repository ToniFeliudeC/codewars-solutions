#When provided with a String, capitalize all vowels

#For example:

#Input : "Hello World!"

#Output : "HEllO WOrld!"

#Note: Y is not a vowel in this kata.

#My solution

def swap(st):

    newString = ""
    
    for i in st:
        if i in "aeiou":
            newString += i.upper()
        else:
            newString += i

    return newString