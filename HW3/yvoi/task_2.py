num = int(input("Enter number: "))
num_list = []

# --- counting the multiplication of elements and reverse

element = 0
multiplication = 1
reverse = 0

while num > 0:
    element = num % 10
    num_list.append(element)     # adding elements in list to use in future
    multiplication *= element    # multiplication elements function
    reverse *= 10                # reverse function
    reverse += element
    num //= 10

print("Multiplication of elements:", multiplication)
print("Reverse:", reverse)

# --- sorting our number

num_list.sort()
sort_num = 0
for x in num_list:
    sort_num *= 10
    sort_num += x
print("Sorted number:", sort_num)