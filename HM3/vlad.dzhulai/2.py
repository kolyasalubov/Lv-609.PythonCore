number = input("Enter 4 digit number: ")

#The first exercise:
n = 1
for i in number:
    n *= int(i)
print(n)

#The second exercise:
print(int(number[::-1]))

#The third exercise:
list_of_ints = [int(item) for item in number]
print(sorted(list_of_ints))
