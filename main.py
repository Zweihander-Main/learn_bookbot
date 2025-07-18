from stats import get_char_data, get_num_words

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
	relative_path = './books/frankenstein.txt'
	book_text = ""
	try:
		book_text = get_book_text(relative_path)
	except FileNotFoundError:
		print(f"Error: The file '{relative_path}' was not found.")
	except Exception as e:
		print(f"An error occurred: {e}")

	if book_text:
		num_words = get_num_words(book_text)
		print(f"{num_words} words found in the document")
		char_data: dict[str, int]	 = get_char_data(book_text)
		print("Character statistics:")
		for char, count in sorted(char_data.items()):
			print(f"'{char}': {count}")
	else:
		print("The book is empty or could not be read.")

if __name__ == "__main__":
	main()
