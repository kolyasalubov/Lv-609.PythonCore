list_with_integers = [1, 2, 3]
list_with_floats = []


for item in list_with_integers:
    item = float(item)
    list_with_floats.append(item)
print(list_with_floats)


list_conver = [1, 2, 3]
list_conver = [float(i) for i in list_conver]
print(list_conver)


l2 = [1, 2, 3]
l2 = list(map(float, l2))
print(l2)


list_with_integerss = [1, 2, 3]
i = 0
for i, item in enumerate(list_with_integerss):
    list_with_integerss[i] = float(item)

print(list_with_integerss)
