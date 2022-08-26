#You live in the city of Cartesia where all roads are laid out in a perfect grid.
#You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk.
#The city provides its citizens with a Walk Generating App on their phones -- everytime you press the button it sends you
#an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']).
#You always walk only a single block for each letter (direction) and you know it takes you one minute to traverse one city 
#block, so create a function that will return true if the walk the app gives you will take you exactly 
#ten minutes (you don't want to be early or late!) and will, of course, return you to your starting point.
#Return false otherwise.

#Note: you will always receive a valid array containing a random assortment of direction letters ('n', 's', 'e', or 'w' only).
#It will never give you an empty array (that's not a walk, that's standing still!).

#My 1st, less efficient, but in my opinion, more understandable solution.

def is_valid_walk(walk):
    
    #We make sure there are 10 direction in the "walk" array.
    #If there are more than 10 we would arrive too late, if there were less we would arrive too early:
    #In both of those cases we would return false and end the funcion.
    if len(walk) == 10: 
        
        #We create an array named "position" which is going to work as our current position coordinates.
        position = [0, 0] # X, Y
        
        #We loop through the "walk" array to see the directions 1 by 1, and change the coordinates X and Y values based on 
        #that specific direction.
        for i in walk:
            if i == "n":
                position[1] += 1
            elif i == "s":
                position[1] -= 1
            elif i == "w":
                position[0] -= 1
            elif i == "e":
                position[0] += 1  
        
        #In case we ended up on the initial position (position == [0, 0]), the walk is valid and we can return True, any other position value,
        #the walk is not valid and we return False   
        return True if position == [0, 0] else False
    
    else:
        return False

#My 2nd solution, way shorter and probably the one that should be applied in a real life project.

def is_valid_walk(walk):
    return len(walk) == 10 and walk.count("n") == walk.count("s") and walk.count("w") == walk.count("e")





