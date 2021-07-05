def even_div_by_2():
	result = set()
	for number in range(1, 11):
		if number % 2 == 0:
			result.add(number)
	return result


def odd_div_by_3():
	result = set()
	for number in range(1, 11):
		if number % 2 != 0 and number % 3 == 0:
			result.add(number)
	return result


def not_div_by_2_3():
	result = set()
	for number in range (1, 11):
		if number % 3 != 0 and number % 2 != 0:
			result.add(number)
	return result


if __name__ == "__main__":
	print(f"Even numbers that are divisible by 2: {even_div_by_2()}", end=f"\n{'-'*54}\n")
	print(f"Odd numbers, which are divisible by 3: {odd_div_by_3()}", end=f"\n{'-'*54}\n")
	print(f"Numbers that are not divisible by 2 and 3: {not_div_by_2_3()}", end=f"\n{'-'*54}\n")

