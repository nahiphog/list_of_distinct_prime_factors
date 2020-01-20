def area_of_triangle_via_heron(first_length, second_length, third_length):
    s = (1/2) * (first_length + second_length + third_length)
    return pow( s * (s- first_length) * (s - second_length) * (s - third_length) , 1/2)

################

# Shoelace formula
def area(x1, y1, x2, y2, x3, y3): 
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0) 

################

# Is a coordinate inside a triangle (Coordinate geometry)?
# Courtesy to https://www.geeksforgeeks.org/check-whether-a-given-point-lies-inside-a-triangle-or-not/

def isInside(x1, y1, x2, y2, x3, y3, x, y): 
    # Calculate area of triangle ABC 
    A = area (x1, y1, x2, y2, x3, y3) 
    # Calculate area of triangle PBC  
    A1 = area (x, y, x2, y2, x3, y3) 
    # Calculate area of triangle PAC  
    A2 = area (x1, y1, x, y, x3, y3) 
    # Calculate area of triangle PAB  
    A3 = area (x1, y1, x2, y2, x, y) 
    # Check if sum of A1, A2 and A3 is same as A 
    if(A == A1 + A2 + A3): 
        return True
    else: 
        return False
