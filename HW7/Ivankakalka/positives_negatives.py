def count_positives_sum_negatives(arr):
    count = 0
    sum = 0
    if arr != []:
        for item in arr:
            if item > 0:
                count += 1
            else:
                sum += item
    else:
        return arr
    arr.clear()
    arr.append(count)
    arr.append(sum)
    return arr
    