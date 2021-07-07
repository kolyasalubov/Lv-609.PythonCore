# 1-st variation
def get_max1(num1: int, num2: int):
	"""
	This named function returns the 
	largest number of two numbers.
	"""
	return max(num1, num2)


# 2-nd variation
def get_max2(*args):
	"""
	This named function returns the 
	largest number of <args> list.
	"""
	return max(args)


# 3-d variation
get_max3 = lambda x, y: max(x, y)  # (1, 5)
"""Unnamed lambda function, that takes 2 arguments
and returns the largest of them"""


if __name__ == "__main__":
	print(f"First method: {get_max1(1, 4)}\n"
		  f"Second method: {get_max2(1, 3, -1, 4, 5, 32, 1, 2)}\n"
		  f"Third method: {get_max3(1, 5)}\n")