#Every book has n pages with page numbers 1 to n. 
#The summary is made by adding up the number of digits of all page numbers.

#Task: Given the summary, find the number of pages n the book has.

#Example
#If the input is summary=25, then the output must be n=17: The numbers 1 to 17 have 25 digits in total: 1234567891011121314151617.

#Be aware that you'll get enormous books having up to 100.000 pages.

#All inputs will be valid.

#My solution

def amount_of_pages(summary):
    
    #We will use and increase the "page" variable to know in which page number
    #we are, so that we can increase the digits variable adding the number of digits
    #the "current page" has.
    page = 1
    digits = 0
    
    #We will keep repeating the process mentioned above
    #until the digits variable value is greater or equal to
    #"summary".
    while digits < summary:
        digits += len(str(page))
        page += 1
    
    #Finally we return the "page" variable having substracted 1 from it, since
    #we started from the page 1, and not 0.
    return page - 1