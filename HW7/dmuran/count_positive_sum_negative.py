def count_positives_sum_negatives(arr):
    count = 0
    sum = 0
    if arr != []:
        for i in arr:
            if i > 0:
                count += 1
            else:
                sum += i
    else:
        return arr
    arr.clear()
    arr.append(count)
    arr.append(sum)
    return arr
