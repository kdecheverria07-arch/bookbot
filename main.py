def get_book_text(filepath):
    """Read a file and return its contents as a string."""
    with open(filepath, 'r') as file:
        return file.read()

from stats import count_words

def main():
    # Get the book text
    book_text = get_book_text("books/frankenstein.txt")
    
    # Count the words using the new function
    num_words = count_words(book_text)
    
    # Print the required message
    print(f"Found {num_words} total words")

# Call main() at the bottom to execute your program
if __name__ == "__main__":
    main()