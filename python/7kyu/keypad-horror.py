#Having two standards for a keypad layout is inconvenient!
#Computer keypad's layout:
#7 8 9  \n
#4 5 6  \n
#1 2 3  \n
#  0 \n

#Cell phone keypad's layout:
#1 2 3\n 
#4 5 6\n  
#7 8 9\n  
#  0\n

#Solve the horror of unstandardized keypads by providing a function that converts computer input to a number as if it was typed on a phone.

#Example:
#"789" -> "123"

#Notes:
#You get a string with numbers only

#My solution

def computer_to_phone(numbers):

    result = ""

    for i in numbers:
        if i == "7" or i == "8" or i == "9":
            result += str(int(i) - 6)
        elif i == "1" or i == "2" or i == "3":
            result += str(int(i) + 6)
        else:
            result += i

    return result

#My 2nd solution

from string import maketrans

def computer_to_phone(numbers):
    return numbers.translate(maketrans("123789", "789123"))