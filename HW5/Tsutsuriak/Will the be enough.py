def enough(cap, on, wait):
    if cap >= on + wait:
        return 0
    if cap < on + wait:
        return abs(cap - on - wait)
