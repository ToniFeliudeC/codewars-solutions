#Given a non-negative integer, return an array / a list of the individual digits in order.

#Examples:

#123 => [1,2,3]

#1 => [1]

#8675309 => [8,6,7,5,3,0,9]

#My solution

def digitize(n):
    return [int(x) for x in str(n)]

#My 2nd solution

def digitize(n):
    
    #This variable will storage our result.
    array = []
    
    #We travel the entire number as an string, digit by digit and append each digit as an (int)
    #to the (array)
    for i in str(n):
        array.append(int(i))
    return array
