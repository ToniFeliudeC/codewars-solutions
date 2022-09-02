#You are going to be given a word.
#Your job will be to make sure that each character in that word has the exact same number 
#of occurrences.
#You will return true if it is valid, or false if it is not.

#For this kata, capitals are considered the same as lowercase letters. Therefore: "A" == "a"

#The input is a string (with no spaces) containing [a-z],[A-Z],[0-9] and common symbols. The length will be 0 < length < 100.

#Examples
#"abcabc" is a valid word because "a" appears twice, "b" appears twice, and"c" appears twice.
#"abcabcd" is NOT a valid word because "a" appears twice, "b" appears twice, "c" appears twice, but "d" only appears once!
#"123abc!" is a valid word because all of the characters only appear once in the word.

#My solution

def validate_word(word):
    
    #The variable "lowercase" will storage the "word" string as lowercase, so that we can work with it as case insensitive.
    #The variable comparison will storage the number of times that the first element (letter) appears in the "word" string, so that
    #we can use it as a comparator for the rest of them.
    lowercase = word.lower()
    comparison = lowercase.count(lowercase[0])
    
    #We travel the entire "lowercase" string and check if the number of times that each letter appears equals to the (comparison) int.
    #In case it does not match, we can instantly return False, however, if we end the entire loop, means that all letters appear the same number of times
    #and we can return True.
    for i in lowercase:
        if lowercase.count(i) != comparison:
            return False
    
    return True