#Create a function called shortcut to remove the lowercase vowels (a, e, i, o, u ) in a given string.

#Examples
#"hello"     -->  "hll"
#"codewars"  -->  "cdwrs"
#"goodbye"   -->  "gdby"
#"HELLO"     -->  "HELLO"
#don't worry about uppercase vowels
#y is not considered a vowel for this kata

#My solution

def shortcut( s ):
    
    #This string will contain our final result.
    newS = ""
    
    #We trabel the entire "s" string and add each element(letter) to the "newS" in case is not a vowel.
    for i in s:
        if i not in "aeiou":
            newS += i
            
    return newS