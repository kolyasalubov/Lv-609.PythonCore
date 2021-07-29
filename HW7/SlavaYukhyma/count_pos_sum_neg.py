def count_positives_sum_negatives(arr):
    result = [0, 0]
    if arr == []:
        return arr
    else:
        for item in arr:
            if item > 0:
                result[0] += 1
            else:
                result[1] += item
    return result
