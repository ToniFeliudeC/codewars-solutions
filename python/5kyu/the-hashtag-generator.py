#The marketing team is spending way too much time typing in hashtags.
#Let's help them with our own Hashtag Generator!

#Here's the deal:

#It must start with a hashtag (#).
#All words must have their first letter capitalized.
#If the final result is longer than 140 chars it must return false.
#If the input or the result is an empty string it must return false.
#Examples
#" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
#"    Hello     World   "                  =>  "#HelloWorld"
#""                                        =>  false

#My solution

def generate_hashtag(s):
    
    #We create an array of string named "brokenText" where each element is going to be every single word of the "s" string, removing all spaces,
    #using the split() function.
    brokenText = s.split()
    
    #This variable will contain our hashtag, we can initialize it with the "#" symbol since it's going to be common for every case.
    hashtag = "#"
    
    #We loop throught each element of brokenText and add it to the "hashtag" string applying the title() function to it, 
    #which capitalizes the first letter of the element (word).
    for i in brokenText:
        hashtag += i.title()
    
    #Once the hashtag string variable is ready, we make sure its length won't exceed 140, or the "s" string wasn't empty on the first place.
    return hashtag if len(hashtag) <= 140 and s != "" else False