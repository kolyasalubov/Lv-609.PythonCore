def count_positives_sum_negatives(arr):
    if not arr:
        return []
    count_pos=[x for x in arr if x > 0]
    count_neg=[x for x in arr if x < 0]
    return [len(count_pos),sum(count_neg)]
