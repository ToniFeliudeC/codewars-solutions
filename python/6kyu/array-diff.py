#Your goal in this kata is to implement a difference function, which subtracts one list from another and 
#returns the result.

#It should remove all values from list a, which are present in list b keeping their order.

#array_diff([1,2],[1]) == [2]
#If a value is present in b, all of its occurrences must be removed from the other:

#array_diff([1,2,2,2,3],[2]) == [1,3]

#My solution

def array_diff(a, b):
    
    #First of all I created a function to check if lists overlap (any element of (a) still exists in (b)).
    def lists_overlap(a, b):
        for i in a:
            if i in b:
                return True
        return False

    #While lists still overlap, we check elements that exist in (a) and (b), and remove them from (a).
    #Once lists stop overlaping, means all elements from (b) that existed in (a) are now removed.
    while lists_overlap(a, b):
        for i in b:
            for j in a:
                if i == j:
                    a.remove(j)

    return a