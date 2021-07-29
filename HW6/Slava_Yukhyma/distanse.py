from math import sqrt


def distance(x1, y1, x2, y2):
    distance = sqrt((x2-x1)**2+(y2-y1)**2)
    return round(distance, 2)


print(distance(1, 2, 3, 4,))
