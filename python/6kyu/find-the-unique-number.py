#There is an array with some numbers. All numbers are equal except for one. Try to find it!

#find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
#find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
#It’s guaranteed that array contains at least 3 numbers.

#The tests contain some very huge arrays, so think about performance.

#My solution

def find_uniq(arr):
    
    #We travel the entire array with a double for to compare each element with each other.
    #Once we found 2 different elements, we check with of both is repeated fewer times in the array.
    for i in arr:
        for j in arr:
            if i != j:
                if arr.count(i) > arr.count(j):
                    return j
                else:
                    return i