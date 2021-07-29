
entered_list = [2, 12, 22, 123]
converted_list = []
for list_element in entered_list:
    converted_list.append(float(list_element))

print(converted_list)


entered_list = input("Enter numbers through the space :")
entered_list = entered_list.split(' ')
converted_list = []
for list_element in entered_list:
    converted_list.append(float(list_element))

print(converted_list)
