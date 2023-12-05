import math

def calculate_distance(x1, y1, x2, y2):
    # This function returns the euclidean distance between two objects
    # a^2 + b^2 = c^2 (original pythagoras)
    # Avståndet mellan två punkter: (x2-x1)^2 + (y2-y1)^2 = (distance)^2
    # distance = sqrt((x2-x1)^2 + (y2-y1)^2))

    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return distance

