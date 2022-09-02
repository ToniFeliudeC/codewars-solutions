#Write a function that takes an array of numbers (integers for the tests) and a target number.
#It should find two different items in the array that, when added together, give the target value. The indices of these items should then be returned in a tuple / list (depending on your language) like so: (index1, index2).

#For the purposes of this kata, some tests may have multiple answers; any valid solutions will be accepted.

#The input will always be valid (numbers will be an array of length 2 or greater, and all of the items will 
#be numbers; target will always be the sum of two different items from that array).

#two_sum([1, 2, 3], 4) # returns [0, 2] or [2, 0]
#My solution

def two_sum(numbers, target):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if j != i and numbers[i] + numbers[j] == target:
                return [i,j]

#We use a double for loop to compare each index with index unless (i) and (j) are equal, since we cannot use the same 
#index twice.
#If the number at the index (i) and the number at the index (j) add up to (target) we can return an array with those
#2 indexes. [i,j]