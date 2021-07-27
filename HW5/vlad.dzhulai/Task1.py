even_numbers = [i for i in range(1, 11) if i % 2 == 0]
odd_numbers_div3 = [i for i in range(1, 11) if i % 3 == 0]
other_numbers = [i for i in range(1, 11) if i not in even_numbers and i not in odd_numbers_div3]
print(f"Here is the list of even numbers: {even_numbers}"\
      f"\nHere is the list of divisible numbers by 3: {odd_numbers_div3}"
      f"\nHere is the list of other numbers: {other_numbers}")
