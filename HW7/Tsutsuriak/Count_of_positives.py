def count_positives_sum_negatives(arr):
    sum = 0
    counter = 0
    a = []
    for i in arr:
        if i > 0:
            counter += 1
        elif i < 0:
            sum += i
    if arr == [] or arr == [0]:
        a = []
    else:
        a.append(counter)
        a.append(sum)
    return  a
