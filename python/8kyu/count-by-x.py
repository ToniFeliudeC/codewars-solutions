#Create a function with two arguments that will return an array of the first (n) multiples of (x).

#Assume both the given number and the number of times to count will be positive numbers greater than 0.

#Return the results as an array (or list in Python, Haskell or Elixir).

#Examples:

#count_by(1,10) #should return [1,2,3,4,5,6,7,8,9,10]
#count_by(2,5) #should return [2,4,6,8,10]

#My solution

def count_by(x, n):
    
    #We create en array where we are going to store the first (n) multiples of (x)
    array = []
    
    #We initialize a variable that's going to work as a counter
    b = 0
    
    #We keep keep adding multiples of (x) to the array until the length of the array is equal to (n)
    while len(array) < n:
        b += x
        array.append(b)
    
    return array