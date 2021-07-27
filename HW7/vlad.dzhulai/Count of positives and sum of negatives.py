def count_positives_sum_negatives(arr):
    positives = 0
    negatives = 0
    for i in arr:
        if i > 0:
            positives += 1
        elif i < 0:
            negatives += i
    if arr == []:
        return []
    else:
        return [positives, int(negatives)]