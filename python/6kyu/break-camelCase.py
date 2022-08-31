#Complete the solution so that the function will break up camel casing, using a space between words.

#Example
#"camelCasing"  =>  "camel Casing"
#"identifier"   =>  "identifier"
#""             =>  ""

#My solution

def solution(s):

    #This variable will store our resulting uncamelcased string.
    newString = ""

    #We travel string, if the element (letter) is not capital, means we are not on a new word yet,
    #so we simply add that same letter to the "newString".
    #If the letter is capital cased, we just add it with a " " before it.
    for i in s:
        if i.isupper():
            newString += " " + i
        else:
            newString += i

    return newString