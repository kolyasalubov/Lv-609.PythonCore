def letters_dict(word: str):
	"""
	This function takes one str type argument,
	and returns the number of characters 
	included in a given string​.
	"""
	return {letter: word.count(letter) for letter in word}


print(letters_dict("hello"))