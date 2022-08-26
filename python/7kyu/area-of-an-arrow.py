#Area of an arrow
#An arrow is formed in a rectangle with sides a and b by joining the bottom corners to the midpoint of the top edge and the centre of the rectangle.
#a and b are integers and > 0

#Write a function which returns the area of the arrow.

#My solution

#As simple as it looks, we just apply the formula to obtain the area of an arrow.

def arrow_area(a, b):
    return (a/2) * (b/2)