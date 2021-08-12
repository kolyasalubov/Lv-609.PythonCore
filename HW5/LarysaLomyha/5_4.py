def enough(cap, on, wait):
    if wait <= cap - on:
        return 0
    else:
        wait = on + wait - cap
        return wait
