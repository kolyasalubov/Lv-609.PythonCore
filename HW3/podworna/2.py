input_number=list(input("Enter the number-"))

product=int(input_number[0])*int(input_number[1])*int(input_number[2])*int(input_number[3])
print(f"Product={product}")
print(f"Reversible number-{input_number[3]}{input_number[2]}{input_number[1]}{input_number[0]}")
sorted_numbers=sorted(input_number)
print(f"Sorted number={sorted_numbers}")