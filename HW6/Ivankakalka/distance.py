def distance(p1,p2):
    if len (p1) != len (p2) or (p1 == [] or p2 == []):
        return -1
    else:
        return (sum([(a - b)** 2 for a, b in zip(p1, p2)]))**0.5
    