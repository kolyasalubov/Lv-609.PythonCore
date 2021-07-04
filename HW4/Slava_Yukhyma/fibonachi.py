
num = 5
list_fibi = [0, 1, 1]


while list_fibi[-1] != num:
    j = list_fibi[-1]+list_fibi[-2]
    list_fibi.append(j)
print(f'solution 1: {list_fibi}')


# 3

num = 5
list_1 = [0, 1, 1]
d = list_1[-1]
for d in list_1:
    if list_1[-1] < num:
        list_1.append(list_1[-1]+list_1[-2])
        d += 1
print(f'solution 2: {list_1}')
