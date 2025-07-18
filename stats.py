def get_num_words(text: str) -> int:
	"""
	Counts the number of words in a given text.

	Args:
		text (str): The text to count words in.

	Returns:
		int: The number of words in the text.
	"""
	return len(text.split())

def get_char_data(text: str) -> dict[str, int]:
	"""
	Calculates character statistics from the given text.

	Args:
		text (str): The text to analyze.

	Returns:
		dict: A dictionary containing character statistics.
	"""
	char_dict: dict[str, int] = {}
	for c in text:
		lower_c = c.lower()
		if lower_c in char_dict:
			char_dict[lower_c] += 1
		else:
			char_dict[lower_c] = 1
	return char_dict



