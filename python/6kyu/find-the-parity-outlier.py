#You are given an array (which will have a length of at least 3, but could be very large) containing integers.
#The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single 
#integer N. Write a method that takes the array as an argument and returns this "outlier" N.

#Examples
#[2, 4, 0, 100, 4, 11, 2602, 36]
#Should return: 11 (the only odd number)

#[160, 3, 1719, 19, 11, 13, -21]
#Should return: 160 (the only even number)

#My solution

def find_outlier(integers):
    
    #Auxiliar function to check if the outlier number is Odd.
    def isOddList():
        even = 0
        for i in integers:
            if i % 2 == 0:
                even += 1
                if even > 1:
                    return True
        return False
    
    #We travel the integers list and, in case the outlier number is odd, we return the first odd number
    #we find.
    #If the outlier number is even, we return the first even number we find.
    if isOddList():
        for i in integers:
            if i % 2 != 0:
                return i
    else:
        for i in integers:
            if i % 2 == 0:
                return i