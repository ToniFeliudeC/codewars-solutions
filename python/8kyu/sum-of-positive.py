#You get an array of numbers, return the sum of all of the positives ones.

#Example [1,-4,7,12] => 1 + 7 + 12 = 20

#Note: if there is nothing to sum, the sum is default to 0.

#My 1st solution

def positive_sum(arr):
    
    #We initialize at 0 a variable named "sum", which is gonna end up being our result after adding each positive number to it.
    sum = 0
    
    #We loop throught each int element of the array, check if it's positive, if so, we add it to the "sum" variable.
    for i in arr:
        if i > 0:
            sum += i
    
    return sum

#My 2nd and more clean solution

def positive_sum(arr):
    return sum(x for x in arr if x > 0)

