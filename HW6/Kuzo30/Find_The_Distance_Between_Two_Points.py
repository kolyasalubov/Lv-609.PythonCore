from math import sqrt, pow
def distance(x1, y1, x2, y2):
    return float("%.2f" %sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2) * 1.0))