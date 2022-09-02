#Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

#For example:

#unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
#unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
#unique_in_order([1,2,2,3,3])       == [1,2,3]

#My solution


def unique_in_order(iterable):
    
    #In "newList" we will storage our result.
    #"variable" is going to storage the last character we put into the "newList" so that we 
    #can check consecutive same characters.
    newList = []
    variable = ""
    
    #We loop through the iterable array and append them into "newList" unless "variable" is equal to that element.
    for i in iterable:
        if str(i) not in variable:
            
            newList.append(i)
            variable = str(i)

    return newList