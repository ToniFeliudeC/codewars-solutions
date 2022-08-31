#Can you find the needle in the haystack?

#Write a function findNeedle() that takes an array full of junk but containing one "needle"

#After your function finds the needle it should return a message (as a string) that says:

#"found the needle at position " plus the index it found the needle, so:

#Example(Input --> Output)

#["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"] --> "found the needle at position 5" 

##I'm going to comment only the second solution since the first one is pretty straightforward.

#My 1st solution

def find_needle(haystack):
    return "found the needle at position " + str(haystack.index("needle"))

#My 2nd solution

def find_needle(haystack):
    #We travel the haystack array untile the element (i) equals "needle", so that we return the index of the element
    #converted into string.
    for i in range(len(haystack)):
        if haystack[i] == "needle":
            return "found the needle at position " + str(i)