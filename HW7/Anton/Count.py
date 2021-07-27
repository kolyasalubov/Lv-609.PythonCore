def count_positives_sum_negatives(arr):
    count = [ i for i in arr if i > 0]
    s = [i for i in arr if i < 0 ]
    res = [len(count), sum(s)]
    return res
