#Given two arrays a and b write a function comp(a, b) (orcompSame(a, b)) that checks whether the two arrays have the "same" elements, with the same multiplicities (the multiplicity of a member is the number of times it appears). "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.

#Examples
#Valid arrays
#a = [121, 144, 19, 161, 19, 144, 19, 11]  
#b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
#comp(a, b) returns true because in b 121 is the square of 11, 14641 is the square of 121, 20736 the square of 144, 361 the square of 19, 25921 the square of 161, and so on. It gets obvious if we write b's elements in terms of squares:

#a = [121, 144, 19, 161, 19, 144, 19, 11] 
#b = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
#Invalid arrays
#If, for example, we change the first number to something else, comp is not returning true anymore:

#a = [121, 144, 19, 161, 19, 144, 19, 11]  
#b = [132, 14641, 20736, 361, 25921, 361, 20736, 361]
#comp(a,b) returns false because in b 132 is not the square of any number of a.

#a = [121, 144, 19, 161, 19, 144, 19, 11]  
#b = [121, 14641, 20736, 36100, 25921, 361, 20736, 361]
#comp(a,b) returns false because in b 36100 is not the square of any number of a.

#Remarks
#a or b might be [] or {} (all languages except R, Shell).
#a or b might be nil or null or None or nothing (except in C++, COBOL, Crystal, D, Dart, Elixir, Fortran, F#, Haskell, Nim, OCaml, Pascal, Perl, PowerShell, Prolog, PureScript, R, Racket, Rust, Shell, Swift).
#If a or b are nil (or null or None, depending on the language), the problem doesn't make sense so return false.

#Note for C
#The two arrays have the same size (> 0) given as parameter in function comp.

#My solution

def comp(array1, array2):
    
    #In case array 1 or array 2 is null, or not both arrays are empty, we simply return False.
    if array1 == None or array2 == None or len(array1) == 0 and len(array2) != 0 or len(array2) == 0 and len(array1) != 0:
        return False
    
    #In case both arrays are empty we return 0.
    elif len(array1) == 0 and len(array2) == 0:
        return True
    
    #We travel they array 1 and check if each element has it's square number version in array 2.
    #In case we find one element which has not an square version in array 2, we return False.
    #Every team we find the square version of a number in array 2, we remove it from array 2, since every number needs
    #its own one, for example, if we have [2, 2] in array 1 and [4] in array 2, we could not use the 4 number for both 2.
    for i in range(len(array1)):
        if array1[i]**2 not in array2:
            return False
        else:
            array2.remove(array1[i]**2)
            
    return True