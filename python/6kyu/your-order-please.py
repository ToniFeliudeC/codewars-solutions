#Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

#Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

#If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

#Examples
#"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
#"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
#""  -->  ""

#My solution

def order(sentence):
    
    #We will create this array whose elements are the words of the "sentence" string splitted (by default, the separator is " ") thanks to the
    #split() function.
    list = sentence.split()
    
    #This "K" variable is going to help us to keep adding the words into the "newSentence" string in the correct order.
    k = 1
    newSentence = ""
    
    #While number of words into "newSentence" string is not equal to the total number of words of the original sentence
    #we will keep looping through the "list" array, and adding the word + " ", if the number into the word matches with "k" variable.
    #Then, we will increase "k" value by 1 so that next time we repeat the process we are going to find the 2nd, 3rd, and so on word.
    while len(newSentence.split()) != len(list):
        for i in list:
            if str(k) in i:
                newSentence += i + " "
                k += 1
    
    #Finally we have to remove the last character of the "newSentence" string before returning it, since we are adding a " " string after
    #each word is added.
    return newSentence[:-1]