def enough(cap, on, wait):
    return 0 if on + wait <= cap else abs(cap - (wait + on))