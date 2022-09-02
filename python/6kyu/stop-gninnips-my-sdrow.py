#Write a function that takes in a string of one or more words, and returns the same string, 
#but with all five or more letter words reversed (Just like the name of this Kata). 
#Strings passed in will consist of only letters and spaces. 
#Spaces will be included only when more than one word is present.

#Examples:

#spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
#spinWords( "This is a test") => returns "This is a test" 
#spinWords( "This is another test" )=> returns "This is rehtona test"

#My solution

def spin_words(sentence):
    
    #We will storage eachg word of "sentence" as an element of "sentenceList" array.
    #The string "newString" will storage our result.
    sentenceList = sentence.split()
    newString = ""
    
    #We loop through each element(word) of sentenceList and add it reversed to newString, in case its length is 5+,
    #or add it not reversed if its lengeth its 4 or -.
    #Additionally, we always add a " " after each word is added to make the spaces.
    #Finally we remove the last character of "newString" since it's always going to be an extra " ".
    for i in range(len(sentenceList)):
        if len(sentenceList[i]) >= 5:
            newString += sentenceList[i][::-1] + " "
        else:
            newString += sentenceList[i] + " "

    return newString[:-1]

#My 2nd solution
#This solution is absurdly ugly and unefficient but I found it funny to leave it here since was one of the firsts
#functions I wrote in my entire carreer.

def spin_words(sentence):
    
    sentenceList = sentence.split()
    
    newString = ""
    
    for i in range(len(sentenceList)):
        if len(sentenceList[i]) >= 5 and len(sentenceList) == 1:
            newString += sentenceList[i][::-1]
        elif len(sentenceList[i]) >= 5 and len(sentenceList) != 1:
            if i == len(sentenceList) - 1:
                newString += sentenceList[i][::-1]
            else:
                newString += sentenceList[i][::-1] + " "
        elif len(sentenceList[i]) < 5 and len(sentenceList) == 1:
            newString += sentenceList[i]
        else:
            if i == len(sentenceList) - 1:
                newString += sentenceList[i]
            else:
                newString += sentenceList[i] + " "
    return newString