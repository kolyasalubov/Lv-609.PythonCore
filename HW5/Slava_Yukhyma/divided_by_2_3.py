

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
