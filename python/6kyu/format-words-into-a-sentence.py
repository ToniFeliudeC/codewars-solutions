#Complete the method so that it formats the words into a single comma separated value. The last word should be separated by the word 'and'
#instead of a comma.
#The method takes in an array of strings and returns a single formatted string.

#Note:

#Empty string values should be ignored.
#Empty arrays or null/nil/None values being passed into the method should result in an empty string being returned.
#Example: (Input --> output)

#['ninja', 'samurai', 'ronin'] --> "ninja, samurai and ronin"
#['ninja', '', 'ronin'] --> "ninja and ronin"
#[] -->""

#My solution

def format_words(words):
    
    #In case the "words" array is null or no words are providen (length of word equals 0), we return an empty string "".
    if not words:
        return ""
    
    #The "newList" array is going to store each non-empty string from "words".
    #The "newString" variable is going to store our final result.
    newList = []
    newString = ""
    
    #We loop through each element(word) from the "words" array and add it to "newList" in case is not an empty string, as said above.
    for r in words:
        if r != "":
            newList.append(r)
    
    #We travel through all "newList" elements and add them into "newString".
    #Based on its index position, we can determine what string should be added after the new element.       
    for i in range(len(newList)):
        if i != len(newList) - 1 and i != len(newList) - 2:
            newString += newList[i] + ", "
        elif i == len(newList) - 1:
            newString += newList[i]
        else:
            newString += newList[i] + " and "
        
    return newString