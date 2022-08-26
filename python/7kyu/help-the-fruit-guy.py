#Our fruit guy has a bag of fruit (represented as an array of strings) where some fruits are rotten. He wants to replace all the rotten pieces of fruit with fresh ones. For example, given ["apple","rottenBanana","apple"] the replaced array should be ["apple","banana","apple"]. Your task is to implement a method that accepts an array of strings containing fruits should returns an array of strings where all the rotten fruits are replaced by good ones.

#Notes
#If the array is null/nil/None or empty you should return empty array ([]).
#The rotten fruit name will be in this camelcase (rottenFruit).
#The returned array should be in lowercase.

#My solution

def remove_rotten(bag_of_fruits):
    
    #In case the bag is empty, or there is no bag at all, we return an empty array
    if bag_of_fruits == None or len(bag_of_fruits) == 0:
        return []
    
    #We create a new array
    newBag = []
    
    #We loop each element of the array looking for rotten fruits
    for i in bag_of_fruits:
        
        #In case fruit is rotten, we remove the "rotten" part and then add the resulting fruit making sure first letter is also lower (since is camelCase)
        if "rotten" in i:
            wordUnrottened = i.replace("rotten", "")
            newBag.append(wordUnrottened.lower())
        #In case the fruit is not rotten, we just add the exact same fruit into the new bag
        else:
            newBag.append(i)
    
    return newBag