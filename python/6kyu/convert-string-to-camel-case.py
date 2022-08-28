#Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).

#Examples
#"the-stealth-warrior" gets converted to "theStealthWarrior"
#"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

#My solution

def to_camel_case(text):
    
    #This variable uses the replace() function to make sure we are always using the same separator, which will make things easier later on.
    #So, in order to do that, replaces all underscore separators for dash separators.
    solidText = text.replace("_","-")
    
    #Now we create an array whose elements are the words of the "solidText" splitted by their "-" separator.
    splitText = solidText.split("-")
    
    #This variable is where our result is going to be stored.
    newString = ""
    
    #We loop through each element of the "splitText" array and add each element to the "newString" variable with the first letter capitalized
    #thanks to the title() function UNLESS it's the first word of the sentence, in which case we don't have to make it capitalized.
    #However, if it's already capitalized, we should add it as it is, since the exercice specifies that it can be PascalCase too, whose only
    #difference to camelCase, is that the first letter of the first word is also capitalized.
    for i in splitText:
        if splitText.index(i) == 0:
            newString += i
        else:
            newString += i.title()
    
    return newString