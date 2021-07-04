#HW3 blank for the task 2 to add to the Git&GitHub repos

natural_number = input("Введіть чотирицифрове натуральне число, будь ласка:")

natural_number = list(natural_number)
#Not necessare operation as appears


# Multiplication of digits
a = int(natural_number[0])
b = int(natural_number[1])
c = int(natural_number[2])
d = int(natural_number[3])

print("Добуток цифр = %d" % (a*b*c*d))


# Reverse digits
#print("Зворотній порядок:",d,c,b,a,sep='')
#or list.reverse
natural_number.reverse()
a = int(natural_number[0])
b = int(natural_number[1])
c = int(natural_number[2])
d = int(natural_number[3])
print("Зворотній порядок: ", a, b, c, d, sep='')

# Sort digits
natural_number.sort()
a = int(natural_number[0])
b = int(natural_number[1])
c = int(natural_number[2])
d = int(natural_number[3])
print("Сортовані цифри: ", a, b, c, d, sep='')
