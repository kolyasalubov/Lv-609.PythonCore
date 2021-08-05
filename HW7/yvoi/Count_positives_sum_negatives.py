def sum_positive(n):
    return [sum(x for x in n if x < 0), sum(1 for x in n if x > 0)] if arr else []
