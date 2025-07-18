def get_num_words(text: str) -> int:
	"""
	Counts the number of words in a given text.

	Args:
		text (str): The text to count words in.

	Returns:
		int: The number of words in the text.
	"""
	return len(text.split())
