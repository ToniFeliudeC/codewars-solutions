#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

#Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in. Additionally, if the number is negative, return 0 (for languages that do have them).

#Note: If the number is a multiple of both 3 and 5, only count it once.

#My solution

def solution(n):

    #In case n is negative we just return 0.
    if n < 0:
        return 0
    #This variable will store all the multiples of 3 or 5 from 1 to n summed up.
    sum = 0

    #We travel all number from 1 to n and, in case is multiple either of 5 or 3, we add it to the "sum" variable.
    for i in range(1,n):
        if i % 3 == 0 or i % 5 == 0:
            sum += i

    return sum