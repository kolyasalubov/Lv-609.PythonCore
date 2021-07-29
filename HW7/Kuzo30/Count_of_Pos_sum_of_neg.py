def count_positives_sum_negatives(arr):
    count_positive = sum(1 for x in arr if x > 0)
    sum_negative = sum(x for x in arr if x < 0)
    return [count_positive, sum_negative] if len(arr) else []