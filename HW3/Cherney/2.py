number = input("Give a 4-digit number ")
if type(number) and len(number)==4:
    #variant_1
    digits_of_number = list(number)
    product_1 = 1
    for x in digits_of_number:
        product_1 *= int(x)
    # variant_2
    first_digit = int(int(number) / 1000)
    second_digit = int((int(number) - first_digit * 1000) / 100)
    third_digit = int((int(number) - first_digit * 1000 - second_digit * 100) / 10)
    fourth_digit = int(number) - first_digit * 1000 - second_digit * 100 - third_digit * 10
    product_2 = first_digit * second_digit * third_digit * fourth_digit

    reverse_1 = "".join(digits_of_number[::-1])
    sort_1 = "".join(sorted(digits_of_number))

    print(f"Product of multiplication is {product_1}",
          f"Reversed number is {reverse_1}",
          f"Sorted number is {sort_1} or",
          sep="\n")
elif type(number):
    print("It has to be a 4-digit number!")
else:
    print("It has to be an integer")