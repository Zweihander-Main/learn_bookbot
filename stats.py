from custom_types import CharDataSortedList, CharDict

def get_num_words(text: str) -> int:
	"""
	Counts the number of words in a given text.

	Args:
		text (str): The text to count words in.

	Returns:
		int: The number of words in the text.
	"""
	return len(text.split())

def get_char_data(text: str) -> CharDict:
	"""
	Calculates character statistics from the given text.

	Args:
		text (str): The text to analyze.

	Returns:
		dict: A dictionary containing character statistics.
	"""
	char_dict: CharDict = {}
	for c in text:
		lower_c = c.lower()
		if lower_c in char_dict:
			char_dict[lower_c] += 1
		else:
			char_dict[lower_c] = 1
	return char_dict

def get_sorted_char_data(d: CharDict) -> CharDataSortedList:
	"""
	Sorts character data from a dictionary into a list of dictionaries.

	Args:
		d (CharDict): A dictionary containing character counts.

	Returns:
		CharDataSortedList: A sorted list of dictionaries with character and count.
	"""
	sorted_list: CharDataSortedList = []
	for char, count in d.items():
		if not char.isalpha():
			continue
		sorted_list.append({"char": char, "num": count})
	sorted_list.sort(key=lambda x: x["num"], reverse=True)
	return sorted_list



