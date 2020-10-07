import math 

class Distance():
    # Function to calculate distance 
    def distance(x1 , y1 , x2 , y2): 
        # Calculating distance 
        return math.sqrt(math.pow(x2 - x1, 2) +math.pow(y2 - y1, 2) * 1.0)

    def pointPairs(points_array)