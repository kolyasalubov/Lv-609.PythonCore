# HW5 Task 1

# In the range from 1 to 10 determine 
# even numbers that are divisible by 2,
# odd numbers, which are divisible by 3,
# numbers that are not divisible by 2 and 3.

range_one_ten = []

for element in range(1,11):
    if element%2 == 0:
        print(element, end=" - ")
        print("Even number divisible by 2")
    elif element%3 == 0:
        print(element, end=" - ")
        print("Odd number divisible by 3")
    else:
        print(element, end=" - ")
        print("Element not divisible by 2 and 3")

#    range_one_ten.append(element)

#print(range_one_ten)

