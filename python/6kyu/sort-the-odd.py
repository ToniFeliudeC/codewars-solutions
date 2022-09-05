#Task
#You will be given an array of numbers.
#You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

#Examples
#[7, 1]  =>  [1, 7]
#[5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
#[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]

#My solution

def sort_array(source_array):
    
    #The "newArray" variable will store our result, while "oddArray" will store all odd numbers that 
    #are into "source_array".
    newArray = []
    oddArray = []
    
    #We travel the entire "source_array" and append every odd number into "oddArray".
    for i in source_array:
        if i % 2 != 0:
            oddArray.append(i)

    #This variable will store the oddArray in an ascending sort order.
    sortedArray = sorted(oddArray)
    
    #Finally we loop through each element of "source_array" and, in case it's even we just add it to the "newArray",
    #but if it's odd, we append the 1st element of "sortedArray" and then remove it, so that we keep adding all the odd
    #numbers in an ascending sorted order.
    for i in source_array:
        if i % 2 == 0:
            newArray.append(i)
        else:
            newArray.append(sortedArray[0])
            sortedArray.pop(0)
            
    return newArray