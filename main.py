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

def get_num_words(text: str) -> int:
	"""
	Counts the number of words in a given text.

	Args:
		text (str): The text to count words in.

	Returns:
		int: The number of words in the text.
	"""
	return len(text.split())

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
	else:
		print("The book is empty or could not be read.")

if __name__ == "__main__":
	main()
