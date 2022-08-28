#Sentence Smash
#Write a function that takes an array of words and smashes them together into a sentence and returns the sentence. You can ignore any need to sanitize words or add punctuation, 
#but you should add spaces between each word. Be careful, there shouldn't be a space at the beginning or the end of the sentence!

#Example
#['hello', 'world', 'this', 'is', 'great']  =>  'hello world this is great'

#My solution

def smash(words):
    
    #We initialize an empty string variable, which is gonna end up storing our resulting string.
    result = ""
    
    #We loop through each string element of the "words" array add it to the "result" variable, with an " " string at the end.
    for i in words:
        result += i + " "
    
    #Finally we return the string removing the last character (which is always going to be an space [" "])
    return result[:-1]