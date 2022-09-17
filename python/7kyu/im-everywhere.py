#Overview
#Many people know that Apple uses the letter "i" in almost all of its devices to emphasize its personality.

#And so John, a programmer at Apple, was given the task of making a program that would add that letter to every word.
#Let's help him do it, too.

#Task:
#Your task is to make a function that takes the value of word and returns it with an "i" at the beginning of the word.
#For example we get the word "Phone", so we must return "iPhone". But we have a few rules:

#The word should not begin with the letter "I", for example Inspire.
#The number of vowels should not be greater than or equal to the number of consonants, for example East or Peace.
#("y" is considered a consonant)
#The first letter should not be lowercase, for example road.
#If the word does not meet the rules, we return "Invalid word".

#My solution

def i(word):
        
    if len(word) == 0 or word[0] == "i" or word[0] == "I":
        return "Invalid word"
    
    vowels = "aeiouAEIOU"
    vowelsCount = 0
    consonantsCount = 0
    newWord = ""
    
    for i in word:
        if i in vowels:
            vowelsCount += 1
        else:
            consonantsCount += 1
            
    if vowelsCount >= consonantsCount or word[0].islower():
        return "Invalid word"
    
    newWord += "i" + word
    
    return newWord

#My 2nd solution, it's so terrible and ugly but I found it funny to leave it here as a comparison since it was one of the
#first code block I ever wrote by myself.

def i(word):
    vowels = "aeiouAEIOU"
    vowelsCount = 0
    consonantsCount = 0
    newWord = ""
    iI = "iI"
    if len(word) == 0:
        return "Invalid word"
    if word[0] == "i" or word[0] == "I":
        return "Invalid word"
    for i in word:
        if i in vowels:
            vowelsCount += 1
        else:
            consonantsCount += 1
    if vowelsCount >= consonantsCount:
        return "Invalid word"
    if word[0].islower():
        return "Invalid word"
    newWord += "i"
    newWord += word
    return newWord