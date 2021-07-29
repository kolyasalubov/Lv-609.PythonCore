import math


def rectangle_square(side_1: float, side_2: float):
	"""
	function takes 2 arguments and returns 
	square of rectangle with such sides
	"""
	return side_1 * side_2


def triangle_square(side_1: float, side_2: float, side_3: float):
	"""
	function takes length of 3 sides of triangle,
	and calculate it's square with a Geron formula.
	"""
	p = (side_1 + side_2 + side_3) / 2
	return math.sqrt(p * (p - side_1) * (p - side_2) * (p - side_3))


def circle_square(rad: float):
	"""
	Function takes radius of a circle 
	and returns it's square.
	"""
	return  math.pi * math.pow(rad, 2)


if __name__ == "__main__":
	print(f"{rectangle_square(2)}\n{triangle_square(3, 4, 5)}\n{circle_square(3)}")