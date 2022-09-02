#Simple, given a string of words, return the length of the shortest word(s).

#String will never be empty and you do not need to account for different data types.

#My solution

def find_short(s):
    
    #The array "wordsLength" will storage the number of letters of each word of the "s" string.
    wordsLength = []

    #We loop through each word of "s" thanks to the "split" function.
    #Then append the length of each word as a new element of "wordsLength" array.
    for i in s.split():
        wordsLength.append(len(i))
    
    #Finally, we return the minimum value of "wordsLength".
    return min(wordsLength)