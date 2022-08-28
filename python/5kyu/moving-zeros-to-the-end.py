#Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

#move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

#My solution

def move_zeros(array):
    
    #We create an empty new array which is going to end up being our result.
    newArray = []
    
    #This variable will be a counter of how many zeros we encounter while looping through all the elements of the array.
    zeros = 0
    
    #We loop through each element of the array and append each element to the "newArray" ONLY if it's not a zero, otherwise we just
    #increase "zeros" variable value by 1.
    for i in array:
        if i != 0:
            newArray.append(i)
        else:
            zeros += 1
    
    #Now we add a 0 at the end of the "newArray" as many times as the value of the variable "zeros".
    for i in range(0,zeros):
        newArray.append(0)
    
    return newArray    