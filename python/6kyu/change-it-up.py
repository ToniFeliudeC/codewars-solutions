#Create a function that takes a string as a parameter and does the following, in this order:

#Replaces every letter with the letter following it in the alphabet (see note below)
#Makes any vowels capital
#Makes any consonants lower case
#Note:

#the alphabet should wrap around, so Z becomes A
#in this kata, y isn't considered as a vowel.
#So, for example the string "Cat30" would return "dbU30" (Cat30 --> Dbu30 --> dbU30)

#My solution

def changer(s):
    
    #The offset string is going to storage the "s" string wit each letter replace with the letter following in the alphabet.
    #The consonants lower is going to storage the "offset" string with all vowels capital and all consonants lower case.
    alphabet = "abcdefghijklmnopqrstuvwxyza"
    offset = ""
    consonantsLower = ""
    
    #We loop through each character of the "s" string and add its following letter on the alphabet to "offset" in case it's a letter.
    #Otherwise we just add the same character, since that would mean it's a digit or a symbol.
    for i in s:
        if i.lower() in alphabet:
            offset += alphabet[alphabet.index(i.lower()) + 1]
        else:
            offset += i
    
    #Finally we make each letter capital or lower case depending on if it's vowel or consonant.
    for i in offset:
        if i in "aeiou":
            consonantsLower += i.upper()
        else:
            consonantsLower += i.lower()
    
    return consonantsLower
