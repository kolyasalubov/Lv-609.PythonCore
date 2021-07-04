list_with_integers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_with_floats = []


for item in list_with_integers:
    item = float(item)
    list_with_floats.append(item)
print(list_with_floats)

# i = 0
# for item in list_with_integers:

#     while i <= len(list_with_integers)+1:
#         #item = float(item)
#         list_with_integers.insert(i, float(item))
#         i += 1
# print(list_with_integers)
