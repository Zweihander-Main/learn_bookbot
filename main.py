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
	try:
		book_text = get_book_text(relative_path)
		print(book_text)
	except FileNotFoundError:
		print(f"Error: The file '{relative_path}' was not found.")
	except Exception as e:
		print(f"An error occurred: {e}")

if __name__ == "__main__":
	main()
