#Write a function that will check if two given characters are the same case.

#If either of the characters is not a letter, return -1
#If both characters are the same case, return 1
#If both characters are letters, but not the same case, return 0
#Examples
#'a' and 'g' returns 1

#'A' and 'C' returns 1

#'b' and 'G' returns 0

#'B' and 'g' returns 0

#'0' and '?' returns -1

#My solution

def same_case(a, b): 
    
    #In case a or b is not a letter we return -1.
    if not a.isalpha() or not b.isalpha():
        return -1
    
    #In case both are uppercase or both are lowercase, we return 1.
    if a.isupper() == b.isupper():
        return 1
    
    #In case they are not same case we return 0.
    if a.isupper() != b.isupper():
        return 0