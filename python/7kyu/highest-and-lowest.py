#In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest 
#number.

#Examples
#high_and_low("1 2 3 4 5")  # return "5 1"
#high_and_low("1 2 -3 4 5") # return "5 -3"
#high_and_low("1 9 3 4 -5") # return "9 -5"
#Notes
#All numbers are valid Int32, no need to validate them.
#There will always be at least one number in the input string.
#Output string must be two numbers separated by a single space, and highest number is first.
#FUNDAMENTALSSTRINGS

#My solution

def high_and_low(numbers):
    
    #The "numbersList" array will store each number from "numbers" as an string, removing all blank spaces " "
    #thanks to the "split()" function.
    #The "numbersIntList" is eventually going to store all the string numbers from "numbersList" as ints instead.
    numbersList = numbers.split()
    numbersIntList = []
    
    #We loop through each element from "numbersList" and append it to numbersIntList as an int.
    for i in numbersList:
        numbersIntList.append(int(i))
    
    #Finally we return an string concatenating the minimum and the maximum values from "numbersIntList" as strings again.
    return str(max(numbersIntList))+" "+str(min(numbersIntList))