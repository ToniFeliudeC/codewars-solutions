#Given an array of integers.

#Return an array, where the first element is the count of positives numbers and the second element is 
#sum of negative numbers. 0 is neither positive nor negative.

#If the input is an empty array or is null, return an empty array.

#Example
#For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].

#My solution

def count_positives_sum_negatives(arr):
    
    #In case arr is None (Null) or length of arr equals 0, we just return an empty array.
    if not arr:
        return []

    positivesCount = 0
    negativesSum = 0
    
    #We loop throught the entire array and check if each element is postive or negative in order to add them or count them
    #into their respective variable.
    for i in arr:
        if i > 0:
            positives += 1
        else:
            negatives += i

    #Finally we return an array with 2 elements: the "positivesCount" and "negativesCount".
    return [positivesCount, negativesSum]