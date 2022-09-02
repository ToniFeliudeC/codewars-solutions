#The goal of this exercise is to convert a string to a new string where each character in the new 
#string is "(" if that character appears only once in the original string, or ")" if that character appears 
#more than once in the original string. 
#Ignore capitalization when determining if a character is a duplicate.

#Examples
#"din"      =>  "((("
#"recede"   =>  "()()()"
#"Success"  =>  ")())())"
#"(( @"     =>  "))((" 

#My solution

def duplicate_encode(word):
    
    newString = ""
    
    #We loop through the letters of the "word" string and check if each letter is counted more than once or not.
    #Based on that, we add ")" or "(" to the "newString"
    for i in word.lower():
        if word.lower().count(i) > 1:
            newString += ")"
        else:
            newString += "("

    return newString