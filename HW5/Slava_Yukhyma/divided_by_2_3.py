
divided_by_three = []
even_nums = []
others_nums = []
for i in [i for i in range(11)]:
    if i % 2 == 0:
        even_nums.append(i)
    elif i % 3 == 0:
        divided_by_three.append(i)
    elif not i % 2 == 0 and not i % 3 == 0:
        others_nums.append(i)

print(divided_by_three,
      even_nums,
      others_nums)

############################################################################################

divided_2 = []
divided_3 = []
another_nums = []

([divided_2.append(i) for i in [i for i in range(11)] if i % 2 == 0])
([divided_3.append(i) for i in [i for i in range(11)] if i % 3 == 0])
([another_nums.append(i)
 for i in [i for i in range(11)] if i % 2 != 0 and i % 3 != 0])
print(divided_2, divided_3, another_nums)
