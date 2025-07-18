from custom_types import CharDataSortedList
from stats import get_char_data, get_num_words, get_sorted_char_data

def get_book_text(file_path: str) -> str:
	"""
	Reads the content of a book from a text file.

	Args:
		file_path (str): The path to the text file containing the book.

	Returns:
		str: The content of the book.
	"""
	with open(file_path, 'r', encoding='utf-8') as file:
		return file.read()

def main() -> None:
	"""
	Main function to execute the book reading functionality.
	"""
	relative_path = 'books/frankenstein.txt'
	book_text = ""

	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {relative_path}...")

	try:
		book_text = get_book_text(relative_path)
	except FileNotFoundError:
		print(f"Error: The file '{relative_path}' was not found.")
		return
	except Exception as e:
		print(f"An error occurred: {e}")
		return

	if not book_text:
		print("The book is empty or could not be read.")
		return

	print("----------- Word Count ----------")
	num_words = get_num_words(book_text)
	print(f"Found {num_words} total words")

	print("--------- Character Count -------")
	char_data: dict[str, int]	 = get_char_data(book_text)
	char_data_sorted: CharDataSortedList = get_sorted_char_data(char_data)
	for char_dict in char_data_sorted:
		print(f"{char_dict['char']}: {char_dict['num']}")

	print("============= END ===============")


if __name__ == "__main__":
	main()
