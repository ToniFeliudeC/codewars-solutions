#Count the number of Duplicates
#Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits 
#that occur more than once in the input string. 
#The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

#Example
#"abcde" -> 0 # no characters repeats more than once
#"aabbcde" -> 2 # 'a' and 'b'
#"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
#"indivisibility" -> 1 # 'i' occurs six times
#"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
#"aA11" -> 2 # 'a' and '1'
#"ABBA" -> 2 # 'A' and 'B' each occur twice

#My solution

def duplicate_count(text):

    #The variable "counter" is going to storage the number of characters that are repeated at least once in the "text" string.
    #The alreadyUsed array is will storage the words that have been already found in the "text" string.
    counter = 0
    alreadyUsed = []
    
    #We loop through the "text" string and check if each letter is already in "alreadyUsed" and it's repeated in the string.
    #If it had not been used, and it appears more than once, we add 1 to "counter" and append the letter to "alreadyUsed",
    #so that we won't be counting it the next time we encounter it.
    for i in text.lower():
        if i not in alreadyUsed and text.lower().count(i) > 1:
            counter += 1
            alreadyUsed.append(i)
    
    return counter