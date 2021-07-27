from math import pi, pow as PI


class My_Module:
	def __init__(self):
		pass


	def rectangle_square():
		"""
		function takes 2 arguments and returns 
		square of rectangle with such sides
		"""
		side_1 = int(input("Enter side a: "))
		side_2 = int(input("Enter side b: "))
		return f"Square of rectangle = {side_1 * side_2}"


	def triangle_square():
		"""
		function takes length of 3 sides of triangle,
		and calculate it's square with a Geron formula.
		"""
		side_1 = int(input("Enter side a: "))
		side_2 = int(input("Enter side b: "))
		return f"Square of triangle = {(side_1 * side_2) / 2}"


	def circle_square():
		"""
		Function takes radius of a circle 
		and returns it's square.
		"""
		rad = int(input("Enter radius: "))
		return  round(pi * pow(rad, 2), 2)
	
		